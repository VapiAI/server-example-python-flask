from .inbound import inbound_bp
from .outbound import outbound_bp
from .custom_llm import custom_llm
from .webhook import webhook
from .function_call import function_call
from flask import request, jsonify
from . import api

# Register blueprints
api.register_blueprint(inbound_bp)
api.register_blueprint(outbound_bp)
api.register_blueprint(custom_llm, url_prefix='/custom-llm')
api.register_blueprint(webhook, url_prefix='/webhook')
api.register_blueprint(function_call, url_prefix='/function-call')
