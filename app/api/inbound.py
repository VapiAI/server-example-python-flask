from flask import Blueprint,request, jsonify, abort
from app.types.vapi import VapiPayload, VapiWebhookEnum, Assistant

inbound_bp = Blueprint('inbound_api', __name__)

@inbound_bp.route('/inbound', methods=['POST'])
def inbound():
    try:
        req_body = request.get_json()
        payload: VapiPayload = req_body['message']
        print(payload['type'])
        print(VapiWebhookEnum.ASSISTANT_REQUEST.value)

        if payload['type'] == VapiWebhookEnum.ASSISTANT_REQUEST.value:
            assistant = payload['call'] if 'call' in payload else None

            if assistant:
                assistant_response: Assistant = {
                    'name': "Paula",
                    'model': {
                        'provider': "openai",
                        'model': "gpt-3.5-turbo",
                        'temperature': 0.7,
                        'systemPrompt': (
                            "You're Paula, an AI assistant who can help user draft beautiful emails to their clients "
                            "based on the user requirements. Then Call sendEmail function to actually send the email."
                        ),
                        'functions': [
                            {
                                'name': "sendEmail",
                                'description': (
                                    "Send email to the given email address and with the given content."
                                ),
                                'parameters': {
                                    'type': "object",
                                    'properties': {
                                        'email': {
                                            'type': "string",
                                            'description': (
                                                "Email to which we want to send the content."
                                            ),
                                        },
                                        'content': {
                                            'type': "string",
                                            'description': (
                                                "Actual Content of the email to be sent."
                                            ),
                                        },
                                    },
                                    'required': ["email"],
                                },
                            },
                        ],
                    },
                    'voice': {
                        'provider': "11labs",
                        'voiceId': "paula",
                    },
                    'firstMessage': "Hi, I'm Paula, your personal email assistant.",
                }
                return jsonify({'assistant': assistant_response})
        else:
            raise ValueError('Unhandled message type')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return "Not found", 404
