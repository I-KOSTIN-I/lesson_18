from flask_restx import Resource, Namespace
from app import models
from app.database import db
from app.schemas.directors import DirectorSchema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = db.session.query(models.Director).all()

        return DirectorSchema(many=True).dump(directors), 200


@directors_ns.route('/<int:director_id>')
class DirectorsView(Resource):
    def get(self, director_id):
        director = db.session.query(models.Director).filter(models.Director.id == director_id).first()

        if director is None:
            return {}, 404

        return DirectorSchema().dump(director), 200
