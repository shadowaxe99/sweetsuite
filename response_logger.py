```python
from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('postgresql://localhost:5432/response_logger')
app = Flask(__name__)
api = Api(app)

class LogResponse(Resource):
    def post(self):
        conn = db_connect.connect()
        investor_email = request.json['InvestorEmail']
        response_status = request.json['ResponseStatus']
        query = conn.execute("insert into response_logger values('{0}','{1}')".format(investor_email, response_status))
        return {'status': 'success'}

api.add_resource(LogResponse, '/logResponse')

if __name__ == '__main__':
     app.run(port='5002')
```