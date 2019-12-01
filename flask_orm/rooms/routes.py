from flask import request
from flask_restful import Resource, marshal_with
from sqlalchemy.exc import IntegrityError

from db import Room, db, Staff
from rooms.parser import room_parser
from rooms.structures import room_structure


class Rooms(Resource):
    method_decorators = [marshal_with(room_structure)]

    def get(self, number=None):
        if number is None:
            args = request.args
            number = args.get("number")
            level = args.get("level")
            status = args.get("status")
            price = args.get("price")
            if number:
                return Room.query.filter_by(number=number).all()
            elif level:
                return Room.query.filter_by(level=level).all()
            elif status:
                return Room.query.filter_by(status=status).all()
            elif price:
                return Room.query.filter_by(price=price).all()
        else:
            return Room.query.filter_by(number=number).all(), 201
        return Room.query.all(), 201

    def post(self):
        data = request.json
        room = Room(**data)
        try:
            db.session.add(room)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return Room.query.all()
    
    def patch(self, number):
        data = request.json
        room = Room.query.get(number)
        room.status = data.get("status")
        db.session.commit()
        return Room.query.all()

    def delete(self, number):
        room = Room.query.get(number)
        db.session.delete(room)
        db.session.commit()
        return Room.query.all()


class RoomStaff(Resource):
    def post(self):
        data = request.json
        room_id = data.get("number")
        staff_id = data.get("passport_id")
        room = Room.query.filter_by(number=room_id).first()
        staff_id = Staff.query.filter_by(passport_id=staff_id).first()
        staff_id.rooms.append(room)
        db.session.commit()
        return 'Successfully added'

    @marshal_with(room_structure)
    def get(self):
        args = room_parser.parse_args(strict=True)
        staff = Staff.query.filter_by(passport_id=args.get("passport_id")).first()
        return staff.rooms
