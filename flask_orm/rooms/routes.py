from flask_restful import Resource, marshal_with, abort
from sqlalchemy.exc import IntegrityError

from db import Room, db, Staff, Tenant
from rooms.parser import room_parser, room_status_parser, room_parser_get, room_staff_parser_get
from rooms.structures import room_structure


class Rooms(Resource):
    @marshal_with(room_structure)
    def get(self, number=None):
        data = room_parser_get.parse_args()
        if number:
            return Room.query.filter_by(number=number).first_or_404()
        elif any(tuple(data.values())):
            return Room.query.filter_by(**{k: v
                                           for k, v in data.items()
                                           if v}).all(), 200
        return Room.query.all(), 200

    def post(self):
        data = room_parser.parse_args()
        if not Room.query.filter_by(number=data["number"]).scalar():
            try:
                db.session.add(Room(**data))
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
            return {"msg": f"Room {data['number']} was added"}
        abort(404, message="Room already exist!")

    def patch(self, number):
        data = room_status_parser.parse_args()
        room = Room.query.get(number)
        tenant_id = Tenant.query.get(data["tenant_id"])
        if room and tenant_id:
            room.status = data["status"]
            room.tenant_id = data["tenant_id"]
            db.session.commit()
            return {"msg": f"Room {number} was updated"}
        abort(404, message="Room or tenant_id not found")

    def delete(self, number):
        if Room.query.filter_by(number=number).scalar():
            room = Room.query.get(number)
            db.session.delete(room)
            db.session.commit()
            return {"message": f"Room {number} was deleted"}
        abort(404, message=f"Room {number} not found!")


class RoomStaff(Resource):
    @marshal_with(room_structure)
    def get(self):
        args = room_staff_parser_get.parse_args(strict=True)
        staff = Staff.query.filter_by(passport_id=args.get("passport_id")).first_or_404()
        return staff.rooms

    def post(self):
        data = room_staff_parser_get.parse_args(strict=True)
        try:
            room = Room.query.filter_by(number=data["number"]).first()
            staff_id = Staff.query.filter_by(passport_id=data["passport_id"]).first()
            print(room, staff_id)
            if room and staff_id:
                staff_id.rooms.append(room)
                db.session.commit()
                return {"message": 'Successfully added'}
            abort(404, message=f"Room {data['number']} or staff with passport_id '{data['passport_id']}' not found!")
        except TypeError:
            return {"message": f"Room {data['number']} or staff with passport_id '{data['passport_id']}' not found!"}
