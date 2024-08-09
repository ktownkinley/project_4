import os

from flask import Flask, render_template
from json import JSONEncoder
from flask_cors import CORS
from bson import json_util, ObjectId
from datetime import datetime

from app.api import images_api_v1

class MongoJsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(obj, ObjectId):
            return str(obj)
        return json_util.default(obj, json_util.CANONICAL_JSON_OPTIONS)


def create_app():

    APP_DIR = os.path.abspath(os.path.dirname(__file__))

    app = Flask(__name__)
    CORS(app)
    app.json_encoder = MongoJsonEncoder
    app.register_blueprint(images_api_v1)

    @app.route("/index.html")
    def welcome():
        return (
            render_template("index.html")
        )
    
    @app.route("/slides.html")
    def presentation():
        return (
            render_template("slides.html")
        )
    
    @app.route("/game.html")
    def game():
        return(
            render_template("game.html")
        )
        
    return app
