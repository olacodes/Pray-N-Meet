import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Config:
    @classmethod
    def configuration(cls):
        return {
            'SQLALCHEMY_DATABASE_URI':os.getenv("DATABASE_URL"),
            'SQLACHEMY_TRACK_MODIFICATIONS':False
        }

