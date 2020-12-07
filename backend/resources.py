from flask_restful import Resource, reqparse, abort

import data.db as db
from data.data_converter import *
from statistics import RequestsStatistics

records = db.data

parser = reqparse.RequestParser()
parser.add_argument(ID_FIELD)
parser.add_argument(TIMESTAMP_FIELD)
parser.add_argument(VALUE_FIELD)

statistics = RequestsStatistics()


def check_args(args, must_fields=DATA_MUST_FIELDS):
    for arg, arg_value in args.items():
        if arg_value is None:
            raise ValueError(f"Request parameters are not correct. '{arg}' parameter is not filled. "
                             f"The following parameters should be filled in request: {str(DATA_MUST_FIELDS)}")


class Record(Resource):

    @staticmethod
    def get(record_id):
        for record in records:
            if record[ID_FIELD] == record_id:
                prepared_record = ReadRecord(record).jsonify()
                statistics.register_get(record_id)
                return prepared_record, 200
        else:
            return abort(404, message=f"Record with id '{record_id}' doesn't exist")

    @staticmethod
    def put(record_id):
        params = parser.parse_args()
        try:
            check_args(params, [VALUE_FIELD, TIMESTAMP_FIELD])
        except ValueError as exc:
            return str(exc), 400
        try:
            transformated_record_id = parse_record_id(record_id)
            transformated_record_timestamp = parse_record_timestamp(params[TIMESTAMP_FIELD])
            transformated_record_value = parse_record_value(params[VALUE_FIELD])
        except ValueError as exc:
            return str(exc), 400
        else:

            for record in records:
                if transformated_record_id == record[ID_FIELD]:
                    record[VALUE_FIELD] = transformated_record_value
                    record[TIMESTAMP_FIELD] = transformated_record_timestamp
                    prepared_record = ReadRecord(record).jsonify()
                    return prepared_record, 200

            record = {
                ID_FIELD: transformated_record_id,
                VALUE_FIELD: transformated_record_value,
                TIMESTAMP_FIELD: transformated_record_timestamp
            }
            records.append(record)
            prepared_record = ReadRecord(record).jsonify()

            return prepared_record, 201

    @staticmethod
    def delete(record_id):
        for pos, record in enumerate(records):
            if record[ID_FIELD] == record_id:
                del records[pos]
                statistics.delete_record_statistics(record_id)
                return f"Record with id '{record_id}' is deleted.", 201
        return abort(404, message=f"Record with id '{record_id}' doesn't exist")


class RecordList(Resource):

    @property
    def records_ids(self):
        ids = [record[ID_FIELD] for record in records]
        return ids

    @staticmethod
    def get():
        prepared_records = []
        for record in records:
            statistics.register_get(record[ID_FIELD])
            prepared_records.append(ReadRecord(record).jsonify())
        return prepared_records, 200

    def post(self):
        params = parser.parse_args()
        try:
            check_args(params)
        except ValueError as exc:
            return str(exc), 400

        try:
            transformated_record_id = parse_record_id(params[ID_FIELD])
            transformated_record_value = parse_record_value(params[VALUE_FIELD])
            transformated_record_timestamp = parse_record_timestamp(params[TIMESTAMP_FIELD])
        except ValueError as exc:
            return str(exc), 400
        else:
            if transformated_record_id not in self.records_ids:
                record = {
                    ID_FIELD: transformated_record_id,
                    VALUE_FIELD: transformated_record_value,
                    TIMESTAMP_FIELD: transformated_record_timestamp
                }
                records.append(record)
                return record, 201
            else:
                return abort(404, message=f"Record with id '{transformated_record_id}' already exists.")


class ReadingsCount(Resource):
    @staticmethod
    def get():
        readings_statistic = {'total_readings': statistics.readings_count}
        return readings_statistic


class ReadingsMean(Resource):
    @staticmethod
    def get():
        if statistics.readings_mean:
            readings_mean = {'readings_mean_by_record_id': statistics.readings_mean}
            return readings_mean, 200
        else:
            return 'No enough statistics to calculate mean for record readings.', 200


class ReadingsVariance(Resource):
    @staticmethod
    def get():
        if statistics.readings_mean:
            readings_variance = {'readings_variance_by_record_id': statistics.variance}
            return readings_variance, 200
        else:
            return 'No enough statistics to calculate mean for record readings.', 200


class Statistics(Resource):
    @staticmethod
    def get():
        readings_statistic = {
            'total_readings': statistics.readings_count,
            'readings_mean': 0,
            'readings_variance': 0
        }
        if statistics.readings_mean:
            readings_statistic['readings_mean'] = statistics.readings_mean
            readings_statistic['readings_variance'] = statistics.readings_variance
        return readings_statistic, 200


class ReadingsCountById(Resource):
    @staticmethod
    def get():
        if statistics.readings_count > 0:
            return {'readings_by_record_id': statistics.records_stats}, 200
        else:
            return 'No enough statistics to calculate mean for record readings.', 200
