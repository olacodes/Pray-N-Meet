import os
from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api
from flask_jwt_extended import (
    JWTManager, jwt_required, 
    create_access_token, get_jwt_identity
)

from .config import db
from .config import Config 
from .routes import initialize_routes


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(Config.configuration())
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') or os.urandom(24)

    # app.config['JWT_SECRET_KEY'] = 'jwtsecretekey'
    jwt = JWTManager(app)

    api = Api(app)
    db.init_app(app)

    
    initialize_routes(api)

    @app.before_first_request
    def create_tables():
        db.create_all()
    
    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)
    

    return app
