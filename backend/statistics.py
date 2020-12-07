
import math


class RequestsStatistics:
    """Take all the statistics calculations of REST API requests."""
    def __init__(self):
        self._records_stats = {}
        self._readings_count = 0

    @property
    def readings_count(self):
        return self._readings_count

    @property
    def records_stats(self):
        return self._records_stats

    @property
    def readings_mean(self):
        if self._readings_count > 0:
            record_readings_mean = 0
            for record_id, record_readings_count in self._records_stats.items():
                record_readings_mean += record_readings_count
            return record_readings_mean / len(self._records_stats)
        else:
            return None

    @property
    def readings_variance(self):
        if self._readings_count > 0:
            mean = self.readings_mean
            record_readings_variance = 0
            for record_readings_count in self._records_stats.values():
                record_readings_variance += (record_readings_count - mean)**2
            return record_readings_variance / len(self._records_stats)
        else:
            return None

    @property
    def standart_deviation(self):
        if self._readings_count > 0:
            return math.sqrt(self.readings_variance)
        else:
            return None

    def register_get(self, record_id):
        self._records_stats.setdefault(record_id, 0)
        self._readings_count += 1
        self._records_stats[record_id] += 1

    def delete_record_statistics(self, record_id):
        if record_id in self.records_stats:
            readings_count = self.records_stats[record_id]
            self._readings_count -= readings_count
            del self.records_stats[record_id]

