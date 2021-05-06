from flask import Flask
from flask import request
from database_ops import DatabaseOperation
from business_logic import BusinessLogic
from flask import Response

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'


@app.route('/create_challange', methods=['POST'])
def create_challange():
    json_body = request.get_json()
    business_logic = BusinessLogic()
    business_logic.create_challange(json_body)

    return "", 201

@app.route('/get_challanges', methods=['GET'])
def get_challanges():
    business_logic = BusinessLogic()

    return Response(business_logic.get_active_challanges(), 200, mimetype='application/json')