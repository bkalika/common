from flask import Blueprint
from flask_restful import Api

from rooms.routes import Rooms, RoomStaff

rooms_bp = Blueprint("rooms", __name__)
api_rooms = Api(rooms_bp)

api_rooms.add_resource(Rooms, '/rooms', '/rooms/<int:number>')
api_rooms.add_resource(RoomStaff, '/rooms_staff')
