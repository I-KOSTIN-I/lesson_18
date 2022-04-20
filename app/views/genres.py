from flask import request
from flask_restx import Resource, Namespace
from app.database import db

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201