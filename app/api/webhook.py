from flask import Blueprint, request, jsonify
from app.functions import get_character_inspiration, get_random_name

webhook = Blueprint('webhook', __name__)


@webhook.route('/', methods=['POST'])
async def webhook_route():
    # Add your logic here

    request_data = request.get_json()
    payload = request_data.get('message')

    if payload['type'] == "function-call":
        response = await function_call_handler(payload)
        return jsonify(response), 201
    elif payload['type'] == "status-update":
        response = await status_update_handler(payload)
        return jsonify(response), 201
    elif payload['type'] == "assistant-request":
        response = await assistant_request_handler(payload)
        return jsonify(response), 201
    elif payload['type'] == "end-of-call-report":
        await end_of_call_report_handler(payload)
        return jsonify({}), 201
    elif payload['type'] == "speech-update":
        response = await speech_update_handler(payload)
        return jsonify(response), 201
    elif payload['type'] == "transcript":
        response = await transcript_handler(payload)
        return jsonify(response), 201
    elif payload['type'] == "hang":
        response = await hang_event_handler(payload)
        return jsonify(response), 201
    else:
        raise ValueError('Unhandled message type')






async def function_call_handler(payload):
    """
    Handle Business logic here.
    You can handle function calls here. The payload will have function name and parameters.
    You can trigger the appropriate function based on your requirements and configurations.
    You can also have a set of validators along with each function which can be used to first validate the parameters and then call the functions.
    Here Assumption is that the functions are handling the fallback cases as well. They should return the appropriate response in case of any error.
    """

    function_call = payload.get('functionCall')

    if not function_call:
        raise ValueError("Invalid Request.")

    name = function_call.get('name')
    parameters = function_call.get('parameters')

    if name == 'getCharacterInspiration':
        return get_character_inspiration.get_character_inspiration(**parameters)
    elif name == 'getRandomName':
        params = get_random_name.NameParams(gender="male", nat="US")
        return get_random_name.get_random_name(params)
    else:
        return None

async def status_update_handler(payload):
    """
    Handle Business logic here.
    Sent during a call whenever the status of the call has changed.
    Possible statuses are: "queued","ringing","in-progress","forwarding","ended".
    You can have certain logic or handlers based on the call status.
    You can also store the information in your database. For example whenever the call gets forwarded.
    """
    return {}



async def end_of_call_report_handler(payload):
    """
    Handle Business logic here.
    You can store the information like summary, typescript, recordingUrl or even the full messages list in the database.
    """
    return

async def speech_update_handler(payload):
    """
    Handle Business logic here.
    Sent during a speech status update during the call. It also lets u know who is speaking.
    You can enable this by passing "speech-update" in the serverMessages array while creating the assistant.
    """
    return {}


async def transcript_handler(payload):
    """
    Handle Business logic here.
    Sent during a call whenever the transcript is available for certain chunk in the stream.
    You can store the transcript in your database or have some other business logic.
    """
    return

async def hang_event_handler(payload):
    """
    Handle Business logic here.
    Sent once the call is terminated by user.
    You can update the database or have some followup actions or workflow triggered.
    """
    return 


async def assistant_request_handler(payload):
    """
    Handle Business logic here.
    You can fetch your database to see if there is an existing assistant associated with this call. If yes, return the assistant.
    You can also fetch some params from your database to create the assistant and return it.
    You can have various predefined static assistant here and return them based on the call details.
    """

    if payload and 'call' in payload:
        assistant = {
            'name': 'Paula',
            'model': {
                'provider': 'openai',
                'model': 'gpt-3.5-turbo',
                'temperature': 0.7,
                'systemPrompt': "You're Paula, an AI assistant who can help user draft beautiful emails to their clients based on the user requirements. Then Call sendEmail function to actually send the email.",
                'functions': [
                    {
                        'name': 'sendEmail',
                        'description': 'Send email to the given email address and with the given content.',
                        'parameters': {
                            'type': 'object',
                            'properties': {
                                'email': {
                                    'type': 'string',
                                    'description': 'Email to which we want to send the content.'
                                },
                                'content': {
                                    'type': 'string',
                                    'description': 'Actual Content of the email to be sent.'
                                }
                            },
                            'required': ['email']
                        }
                    }
                ]
            },
            'voice': {
                'provider': '11labs',
                'voiceId': 'paula'
            },
            'firstMessage': "Hi, I'm Paula, your personal email assistant."
        }
        return {'assistant': assistant}

    raise ValueError('Invalid call details provided.')










