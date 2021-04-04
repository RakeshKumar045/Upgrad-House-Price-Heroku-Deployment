import joblib
from flask import Flask, request, jsonify
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
model = joblib.load('hp_trained_model.pkl')


class ParameterSchema(Schema):
    sqft = fields.Integer(required=True)
    place = fields.Integer(required=True)
    yearsOld = fields.Integer(required=True)
    totalFloor = fields.Integer(required=True)
    bhk = fields.Integer(required=True)


@app.route('/')
def index():
    return 'Hello Data Scientists'


@app.route('/house_pred', methods=['POST'])
def predict():
    # Get Request body from JSON
    request_data = request.json
    schema = ParameterSchema()

    try:
        # Validate request body against schema data types
        reqParam = schema.load(request_data)
    except ValidationError as err:
        # Return a nice message if validation fails
        return jsonify(err.messages), 400

    # Convert request body back to JSON str
    area_sqft = reqParam['sqft']
    place = reqParam['place']
    yearsOld = reqParam['yearsOld']
    totalFloor = reqParam['totalFloor']
    bhk = reqParam['bhk']

    returnJson = {}
    # predicting from model
    returnJson['price'] = model.predict(
        [[
            area_sqft,
            place,
            yearsOld,
            totalFloor,
            bhk,
        ]]
    )[0]

    return jsonify(returnJson)


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
