from flask import Flask
from flask_restx import Api

from app.config import Config
from app.database import db
from app.views.directors import directors_ns
from app.views.genres import genres_ns
from app.views.movies import movies_ns


def create_app():
    """функция создания основного объекта application"""
    application = Flask(__name__)
    application.config.from_object(Config)
    application.app_context().push()
    return application


def register_extensions(application: Flask):
    """функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)"""
    db.init_app(application)
    db.create_all()
    api = Api(application, prefix='/api')
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(genres_ns)
    # create_data(app, db)


# функция
# def create_data(application, db):
#   with app.app_context():
#      db.create_all()
#
# создать несколько сущностей чтобы добавить их в БД
#
#        with db.session.begin():
#          db.session.add_all(здесь список созданных объектов)
#
#

if __name__ == '__main__':
    app_config = Config()
    app_ = create_app(app_config)
    register_extensions(app_)
    app_.run()
