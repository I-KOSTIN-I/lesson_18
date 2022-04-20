from flask_restx import Resource, Namespace
from app.database import db
from app.schemas.movies import MovieSchema
from app import models
from flask import request


movies_ns = Namespace('movies')

movie_schema = MovieSchema()


@movies_ns.route('/<int:uid>')
class MovieView(Resource):

    def get(self, uid: int):
        return movie_schema.dump(db.session.guery(models.Movie).filter(models.Movie.id == uid).first()), 200


    def post(self):
        return "", 201


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        return movie_schema.dump(db.session.query(models.Movie).all(), many=True), 200

    def post(self):
        req_json = request.json
        new_movie = models.Movie(**req_json)
        return "", 201
