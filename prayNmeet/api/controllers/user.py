from typing import Dict, List
from werkzeug.security import generate_password_hash, check_password_hash
from flask import Response, request, jsonify
from flask_restful import Resource, reqparse
from ..models.user import User
import json
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity,
    create_refresh_token
)


class UsersApi(Resource):

    @jwt_required
    def get(self) -> Dict:
        current_user = get_jwt_identity()
        print(current_user)
        users = User.query.all()
        return {'users': [user.jsons() for user in users]}
    
    def post(self):
        body = request.get_json(force=True)
        print(body['username'])
        return {'good': 'good'} 

 
class UserApi(Resource):
    def delete(self, id):
        pass

    def put(self, id):
        pass

    def get(self, id):
        pass


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type=str, required=True,
        help='This field cannot be blank'
    )
    parser.add_argument('password', 
        type=str, required=True,
        help='This field cannot be blank'
    )
    parser.add_argument('email', 
        type=str, required=True,
        help='This field cannot be blank'
    )

    def post(self) -> Dict:
        data = UserRegister.parser.parse_args()

        username = data['username']
        
        if User.find_by_username(username):
            return { "message": "A user with {} already exist".format(username)}, 400

        password = data['password']

        hash_password = generate_password_hash(password)
        email = data['email']
        
        user = User(username=username, password=hash_password, email=email)
        user.save_to_db()

        return ({'message': 'Successfully registered' }), 201


class UserLogin(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('username', 
        type=str, required=True,
        help='This field cannot be blank'
    )
    parser.add_argument('password', 
        type=str, required=True,
        help='This field cannot be blank'
    )

    def post(self) -> Dict:
        data = UserLogin.parser.parse_args()

        username = data['username']
        password = data['password']

        if not username:
            return ({'message': 'Missing username parameter'}), 400
        if not password:
            return ({'message': 'Missing password parameter'}), 400

        current_user = User.find_by_username(username=username)
    	
        print(current_user)

        if not current_user or not check_password_hash(current_user.password, password):
            return ({'message': 'Login credentials are invalid'}), 401

        access_token = create_access_token(identity=username, fresh=True)
        refresh_token = create_refresh_token(username)
        return ({'access_token':access_token, 'refresh_token': refresh_token}), 200

 