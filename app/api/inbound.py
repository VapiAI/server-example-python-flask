from flask import jsonify, Blueprint

inbound_bp = Blueprint('inbound_api', __name__)

@inbound_bp.route('/inbound', methods=['POST'])
def inbound():
    # Your logic for handling inbound requests
    return jsonify({"message": "Inbound data received"}), 201