import os
from flask import Flask
# from your_blueprint import your_blueprint  # Replace with your actual blueprint import

app = Flask(__name__)

# Register Blueprints
# app.register_blueprint(your_blueprint, url_prefix='/your_prefix')  # Replace with your actual blueprint and prefix

# Define routes
@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))  # Get port from environment variable or fallback to 5000
    app.run(port=port)