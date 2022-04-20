from flask import request
from flask_restx import Resource, Namespace
from app.database import db

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        return "", 200

    def post(self):
        return "", 201