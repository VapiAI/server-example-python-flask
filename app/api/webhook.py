from flask import Blueprint

webhook = Blueprint('webhook', __name__)


@webhook.route('/', methods=['POST'])
def webhook_route():
    # Add your logic here
    return 'Response from webhook', 200
