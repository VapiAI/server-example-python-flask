from .inbound import inbound_bp
from .outbound import outbound_bp
from flask import request, jsonify
from . import api

# Register blueprints
api.register_blueprint(inbound_bp)
api.register_blueprint(outbound_bp)
