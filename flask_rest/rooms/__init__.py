from flask import Blueprint
from flask_restful import Api

from flask_rest.rooms.rooms import Room

rooms_bp = Blueprint('rooms', __name__)
api = Api(rooms_bp)
api.add_resource(Room, '/rooms', '/rooms/<int:status>')
