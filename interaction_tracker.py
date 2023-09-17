```python
from flask import Flask, request
from flask_restful import Resource, Api
from data_storage import update_interaction

app = Flask(__name__)
api = Api(app)

class InteractionTracker(Resource):
    def post(self):
        data = request.get_json()
        investor_email = data['InvestorEmail']
        open_status = data['OpenStatus']
        click_status = data['ClickStatus']
        response_status = data['ResponseStatus']
        update_interaction(investor_email, open_status, click_status, response_status)
        return {'message': 'Interaction tracked successfully'}, 200

api.add_resource(InteractionTracker, '/trackInteraction')

if __name__ == '__main__':
    app.run(debug=True)
```