import os
import requests
from flask import Blueprint, request, jsonify

outbound_bp = Blueprint('outbound_api', __name__)


VAPI_BASE_URL = os.environ.get("VAPI_BASE_URL", "https://api.vapi.ai")
VAPI_API_KEY= os.environ.get("VAPI_API_KEY", "")

@outbound_bp.route('/outbound', methods=['POST'])
def outbound_route():
    data = request.get_json()
    phoneNumberId = data["phoneNumberId"]
    assistantId = data["assistantId"]
    customerNumber = data["customerNumber"]

    try:
        # Handle Outbound Call logic here.
        # This can initiate an outbound call to a customer's phonenumber using Vapi.

        response = requests.post(
            f"{VAPI_BASE_URL}/call/phone",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {VAPI_API_KEY}",
            },
            json={
                "phoneNumberId": phoneNumberId,
                "assistantId": assistantId,
                "customer": {
                    "number": customerNumber,
                },
            },
        )

        response.raise_for_status()

        data = response.json()
        return jsonify(data), 200
    except requests.exceptions.RequestException as error:
        return jsonify(
            {
                "message": "Failed to place outbound call",
                "error": str(error),
            }
        ), 500
