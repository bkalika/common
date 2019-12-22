from flask_restful import Resource, marshal_with, abort
from sqlalchemy.exc import IntegrityError

from db import Staff, db
from staff.parser import staff_parser_get, staff_parser
from staff.structures import staff_structure


class StaffView(Resource):
    @marshal_with(staff_structure)
    def get(self, passport_id=None):
        data = staff_parser_get.parse_args()
        if passport_id:
            return Staff.query.filter_by(passport_id=passport_id).first_or_404()
        elif any(tuple(data.values())):
            return Staff.query.filter_by(**{k: v
                                            for k, v in data.items()
                                            if v}).all(), 200
        return Staff.query.all(), 200

    def post(self):
        data = staff_parser.parse_args()
        if not Staff.query.filter_by(passport_id=data['passport_id']).scalar():
            try:
                db.session.add(Staff(**data))
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
            return {"message": f"Staff with passport_id {data['passport_id']} was added!"}
        abort(404, message=f"Staff with {data['passport_id']} already exist!")

    def patch(self, passport_id):
        data = staff_parser_get.parse_args()
        staff = Staff.query.get(passport_id)
        if staff:
            staff.position = data["position"]
            staff.salary = data["salary"]
            db.session.commit()
            return {"message": f"Staff {staff} was updated!"}
        abort(404, message="Staff not found!")

    def delete(self, passport_id):
        if Staff.query.filter_by(passport_id=passport_id).scalar():
            staff = Staff.query.get(passport_id)
            db.session.delete(staff)
            db.session.commit()
            return {"message": f"Staff with passport_id {passport_id} was fired!"}
        abort(404, message=f"Staff with passport_id {passport_id} not found!")
