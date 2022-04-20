from flask_restx import Resource, Namespace
from app.database import db
from app.schemas.movies import MovieSchema
from app import models
from flask import request

movies_ns = Namespace('movies')

movie_schema = MovieSchema()


@movies_ns.route('/<int:uid>')
class MoviesView(Resource):
    def get(self, movie_id):
        movie = db.session.query(models.Movie).filter(models.Movie.id == movie_id).first()

        if movie is None:
            return {}, 404

        return movie_schema.dump(movie), 200

    def put(self, movie_id):
        db.session.query(models.Movie).filter(models.Movie.id == movie_id).update(request.json)
        db.session.commit()

        return None, 204

    def delete(self, movie_id):
        db.session.query(models.Movie).filter(models.Movie.id == movie_id).delete()
        db.session.commit()

        return None, 200


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        movies = db.session.query(models.Movie)

        args = request.args

        director_id = args.get('director_id')
        if director_id is not None:
            movies = movies.filter(models.Movie.director_id == director_id)

        genre_id = args.get('genre_id')
        if genre_id is not None:
            movies = movies.filter(models.Movie.genre_id == genre_id)

        movies = movies.all()

        return movie_schema.dump(movies), 200

    def post(self):
        movie = movie_schema.load(request.json)
        db.session.add(models.Movie(**movie))
        db.session.commit()

        return None, 201
