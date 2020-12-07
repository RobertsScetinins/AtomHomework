
URL for service - http://localhost:5000/

Endpoints:
http://localhost:5000/api/v1/records - GET and POST(id, value, timestamp) to create new record
http://localhost:5000/api/v1/records/<int:record_id> - GET, PUT(value, timestamp(%Y-%m-%dT%H:%M:%S)), DELETE
http://localhost:5000/api/v1/statistics - GET
http://localhost:5000/api/v1/statistics/readings_count - GET
http://localhost:5000/api/v1/statistics/readings_mean - GET
http://localhost:5000/api/v1/statistics/readings_variance - GET
http://localhost:5000/api/v1/statistics/readings_count_by_id - GET
