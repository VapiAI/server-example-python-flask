from flask import Blueprint

function_call = Blueprint('function_call', __name__)


@function_call.route('/basic', methods=['POST'])
def basic_functions_route():
    # Add your logic here
    return 'Response from functions/basic', 200



@function_call.route('/rag', methods=['POST'])
def rag_functions_route():
    # Add your logic here
    return 'Response from functions/rag', 200
