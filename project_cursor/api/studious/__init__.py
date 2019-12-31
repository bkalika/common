from flask_restful import Api
from flask import Blueprint

from api.films.resource import StudiosResource

studios_blueprint = Blueprint("films", __name__)
films_api = Api(studios_blueprint)

films_api.add_resource(StudiosResource, 'studio')
