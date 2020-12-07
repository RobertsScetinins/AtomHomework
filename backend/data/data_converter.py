
"""Module provides conversions for request fields."""
from datetime import datetime

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'

ID_FIELD = 'id'
VALUE_FIELD = 'value'
TIMESTAMP_FIELD = 'timestamp'

DATA_MUST_FIELDS = [ID_FIELD, VALUE_FIELD, TIMESTAMP_FIELD]


class Record:
    def __init__(self, record: dict):
        self.id = record['id']
        self.value = record['value']
        self.timestamp = record['timestamp']


class ReadRecord(Record):
    def __init__(self, record: dict):
        super().__init__(record)

    def jsonify(self):
        jsonified_record = {
            'id': self.id,
            'value': self.value,
            'timestamp': self.timestamp.isoformat()
        }
        return jsonified_record


def parse_record_id(record_id) -> int:
    """Transform id to integer.

    Args:
        record_id: Id of record.
    
    Returns:
        Transformated integer value.

    Raises:
        ValueError: If transformation to integer is not possible.
    """
    try:
        transformed_id = int(record_id)
    except ValueError:
        raise ValueError(f"Record 'id' parameter is not a number. Given value: '{record_id}'.")
    else:
        return transformed_id


def parse_record_value(record_value) -> float:
    try:
        transfomed_value = float(record_value)
    except ValueError:
        raise ValueError(f"Record 'value' field is not a float. Given value: '{record_value}'.")
    else:
        return transfomed_value


def parse_record_timestamp(record_timestamp) -> datetime:
    try:
        timestamp_value = datetime.strptime(record_timestamp, '%Y-%m-%dT%H:%M:%S')
    except ValueError:
        raise ValueError(f"Record 'timestamp' value is incorrect. Given value: '{record_timestamp}'."
                         f"Proper datetime format: {DATETIME_FORMAT} ")
    else:
        return timestamp_value
