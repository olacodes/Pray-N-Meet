from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object("api.config.Config")
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(128), nullable=True)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, username):
        self.username = username


@app.route("/")
def hello_world():
    return jsonify(hello="world")
