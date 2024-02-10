from flask import Blueprint, jsonify, request
from app.functions import get_character_inspiration, get_random_name

function_call = Blueprint('function_call', __name__)


@function_call.route('/basic', methods=['POST'])
def basic_functions_route():
    request_data = request.get_json()
    payload = request_data.get('message')

    if payload['type'] == "function-call":
        function_call = payload.get('functionCall')

        if not function_call:
            raise ValueError("Invalid Request.")

        name = function_call.get('name')
        parameters = function_call.get('parameters')
        if name == 'getRandomName':
            params = get_random_name.NameParams(gender="male", nat="US")
            return jsonify(get_random_name.get_random_name(params)), 201
        else:
            return jsonify({}), 201
    else:
        raise ValueError('Unhandled message type')




@function_call.route('/rag', methods=['POST'])
def rag_functions_route():
    request_data = request.get_json()
    payload = request_data.get('message')

    if payload['type'] == "function-call":
        function_call = payload.get('functionCall')

        if not function_call:
            raise ValueError("Invalid Request.")

        name = function_call.get('name')
        parameters = function_call.get('parameters')

        if name == 'getCharacterInspiration':
            return jsonify(get_character_inspiration.get_character_inspiration(**parameters)), 201
        else:
            return jsonify({}), 201
    else:
        raise ValueError('Unhandled message type')

