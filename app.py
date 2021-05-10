from flask import Flask
from flask import request
from database_ops import DatabaseOperation
from business_logic import BusinessLogic
from flask import Response

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'pong'


@app.route('/create_challenge', methods=['POST'])
def create_challenge():
    json_body = request.get_json()
    business_logic = BusinessLogic()
    business_logic.create_challenge(json_body)

    return "", 201

@app.route('/delete_challenges/<int:id>', methods=['DELETE'])
def delete_challenge(id):
    business_logic = BusinessLogic()
    status, message = business_logic.delete_challenge(id)
    response = {}
    if not status:
        response["error"] = message
        return response, 500
    
    else:
        response["success"] = message
        return response, 200

@app.route("/update_challenge/<int:id>", methods=['PUT'])
def update_challenge(id):
    json_body = request.get_json()
    business_logic = BusinessLogic()
    status, message = business_logic.update_challenge(id, json_body)

    response = {}
    if not status:
        response["error"] = message
        return response, 500
    
    else:
        response["success"] = message
        return response, 201


@app.route('/accept_challenge', methods=['POST'])
def accept_challenge():
    json_body = request.get_json()
    business_logic = BusinessLogic()
    business_logic.accept_challenge(json_body)

    return "", 201


@app.route('/get_challenges', methods=['GET'])
def get_challenges():
    business_logic = BusinessLogic()

    return Response(business_logic.get_active_challenges(), 200, mimetype='application/json')


@app.route('/get_users', methods=['GET'])
def get_users():
    business_logic = BusinessLogic()

    return Response(business_logic.get_users(), 200, mimetype='application/json')

@app.route('/get_accepted_challenges', methods=['GET'])
def get_accepted_challenges():
    business_logic = BusinessLogic()

    return Response(business_logic.get_accepted_challenges(), 200, mimetype='application/json')
