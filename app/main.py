import os
import logging
from flask import Flask, request
from .api import api as api_blueprint

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Register Blueprints
app.register_blueprint(api_blueprint, url_prefix='/api')

# Define routes
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # Get port from environment variable or fallback to 5000
    app.run(port=port, debug=True)