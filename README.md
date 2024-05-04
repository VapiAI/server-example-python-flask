# Server-Side Example Python Flask

This repository hosts a Python Flask application that demonstrates server-side operations with Flask. This project is structured to provide a straightforward example of how to manage API integrations and environment configurations.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.6 or higher
- Poetry for dependency management

## Installation

To install the necessary libraries and setup the project environment, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/VapiAI/server-side-example-python-flask.git
2. Navigate to the project directory:
   ```bash
    cd server-side-example-python-flask
3. Install dependencies using Poetry:
    ```bash
     poetry install
## Configuring Environment Variables
This project requires certain environment variables to be set. Create a .env file in the root directory of your project and add the following keys:
  
  ```bash
  WEATHER_API_KEY=<your_weather_api_key_here>
  OPENAI_API_KEY=<your_openai_api_key_here>
  VAPI_BASE_URL=https://api.vapi.ai
  VAPI_API_KEY=<your_vapi_api_key_here>
  ```

Replace <your_weather_api_key_here>, <your_openai_api_key_here>, and <your_vapi_api_key_here> with the actual API keys.

## Running the Project
To run the project, use Poetry to handle the environment:

  ```bash
  poetry run flask run
  ```

This command starts the Flask server on http://127.0.0.1:5000/. You can access the server from your web browser at this address.

