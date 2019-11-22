import json

from flask import Response, request
from flask_restful import Resource

from flask_rest.rooms.arg_parser import marshal_with_decor
from flask_rest.rooms.models import Room
from flask_rest.utils import read_data, write_data

json_file = 'rooms/rooms.json'


class Rooms(Resource):
    @marshal_with_decor
    def get(self):
        json_data = read_data(json_file)
        # room_info = [{
        #     "number": room.number,
        #     "level": room.level,
        #     "status": room.status,
        #     "price": room.price
        # } for room in json_data]
        data = json.dumps(json_data)
        return Response(data, status=200)

    @marshal_with_decor
    def post(self):
        data = request.json
        rooms_data = json.load(open(json_file))
        rooms_data.append(Room(
            data["number"],
            data["level"],
            data["status"],
            data["price"],
        ).to_dict())
        write_data(rooms_data, json_file)
        return rooms_data

    def patсh(self):
        # data = request.json
        # rooms_data = json.load(open(json_file))
        # update_room = rooms_data.get("number")
        # update_room2 = rooms_data.get("number")
        # rooms_data.remove(update_room)
        # rooms_data.insert(update_room2-1, update_room)
        return "path"

    def put(self):
        return "put"

    def delete(self):
        return "del"
