from flask import Blueprint
from flask_restful import Api

from rooms.routes import Rooms

rooms_bp = Blueprint('rooms', __name__)
api = Api(rooms_bp)
api.add_resource(Rooms, '/rooms', '/rooms/<int:status>')
