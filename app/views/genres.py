from flask import request
from flask_restx import Resource, Namespace
from app.database import db
from app import models
from app.schemas.genres import GenreSchema

genres_ns = Namespace('genres')

genre_schema = GenreSchema()


@genres_ns.route('/')
class GenreView(Resource):
    def get(self):
        genres = db.session.query(models.Genre).all()

        return genre_schema.dump(genres), 200


@genres_ns.route('/<int:genre_id>')
class GenreView(Resource):
    def get(self, genre_id):
        genre = db.session.query(models.Genre).filter(models.Genre.id == genre_id).first()

        if genre is None:
            return {}, 404

        return genre_schema.dump(genre), 200
