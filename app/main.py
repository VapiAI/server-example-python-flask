import os
import logging
from flask import Flask, request
from .api import api as api_blueprint
from flask_cors import CORS

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)


# Configure logging
logging.basicConfig(level=logging.INFO)

# Register Blueprints
app.register_blueprint(api_blueprint, url_prefix='/api')

# Define routes
@app.get('/')
def index():
    return {"hi": "Hello, World!"}



# List all registered endpoints
def list_endpoints():
    output = []
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            methods = ','.join(rule.methods)
            output.append((rule.rule, methods))
    return output


# Print the list of registered endpoints to the terminal
endpoints = list_endpoints()
for endpoint in endpoints:
    print(f"Endpoint: {endpoint[0]}, Methods: {endpoint[1]}")


def main():
    port = int(os.getenv('PORT', 8000))  # Get port from environment variable or fallback to 5000
    print(f"Port: {port}")

    app.run(port=port, debug=True)

if __name__ == '__main__':
    main()
