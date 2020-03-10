from .helpers import username_regex, password_regex, email_regex, Helper
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import reqparse
from flask import request
# from .controllers.user import UserLogin



class UserValidation:
    
    # @classmethod
    # def login(cls, func):
    #     @wraps(func)
    #     def wrapper(*args, **kwargs):
    #         username = request.form.get('username')
    #         password = request.form.get('password')
    #         if not Helper.regex_validator(username, username_regex):
    #             return {"message": "username must not be less than 3 characters"}
    #         if not Helper.validate_password(password, password_regex):
    #             return  
                

    @classmethod
    def validate_username(cls, username):
        if not Helper.regex_validator(username, username_regex):
            return {"message": "Invalid email address"}

            return True


    @classmethod
    def validate_password(cls, password):
        pass

    
    @classmethod
    def validate_email(cls, email):
        if not Helper.regex_validator(email, email_regex):
            return {"message": "Invalid email address"}
        return True
        