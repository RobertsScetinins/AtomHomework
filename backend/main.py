from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
from resources import RecordList, Record, ReadingsCount, ReadingsMean, ReadingsVariance, Statistics, ReadingsCountById

app_service = Flask(__name__)
api = Api(app_service)
CORS(app_service)


api.add_resource(RecordList, '/api/v1/records')
api.add_resource(Record, '/api/v1/records/<int:record_id>')
api.add_resource(Statistics, '/api/v1/statistics')
api.add_resource(ReadingsCount, '/api/v1/statistics/readings_count')
api.add_resource(ReadingsMean, '/api/v1/statistics/readings_mean')
api.add_resource(ReadingsVariance, '/api/v1/statistics/readings_variance')
api.add_resource(ReadingsCountById, '/api/v1/statistics/readings_count_by_id')

if __name__ == '__main__':
    app_service.run(host='0.0.0.0')
