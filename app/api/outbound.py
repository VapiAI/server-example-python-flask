from flask import jsonify, Blueprint

outbound_bp = Blueprint('outbound_api', __name__)

@outbound_bp.route('/outbound', methods=['POST'])
def outbound():
    # Your logic for handling outbound requests
    return jsonify({"message": "Outbound data sent"}), 200