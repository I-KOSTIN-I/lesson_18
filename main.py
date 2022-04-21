from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.views.directors import directors_ns
from app.views.genres import genres_ns
from app.views.movies import movies_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)


app = create_app(Config())

if __name__ == '__main__':
    app.run(debug=True)
