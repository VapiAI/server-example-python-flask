from flask import Blueprint

outbound_bp = Blueprint('outbound_api', __name__)

@outbound_bp.route('/outbound', methods=['POST'])
def outbound_route():
    # Add your logic here
    return 'Response from outbound', 200
