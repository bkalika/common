from flask import request
from flask_restful import Resource, marshal_with
from sqlalchemy.exc import IntegrityError

from db import Staff, db
from staff.structures import staff_structure


class StaffView(Resource):
    method_decorators = [marshal_with(staff_structure)]

    def get(self, passport_id=None):
        if passport_id is None:
            args = request.args
            passport_id = args.get("passport_id")
            name = args.get("name")
            position = args.get("position")
            salary = args.get("salary")
            if passport_id:
                return Staff.query.filter_by(passport_id=passport_id).all()
            elif name:
                return Staff.query.filter_by(name=name).all()
            elif position:
                return Staff.query.filter_by(position=position).all()
            elif salary:
                return Staff.query.filter_by(salary=salary).all()
        else:
            return Staff.query.filter_by(passport_id=passport_id).all(), 201
        return Staff.query.all(), 201

    def post(self):
        data = request.json
        staff = Staff(**data)
        try:
            db.session.add(staff)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return Staff.query.all()

    def patch(self, passport_id):
        data = request.json
        staff = Staff.query.get(passport_id)
        staff.position = data.get("position")
        staff.salary = data.get("salary")
        db.session.commit()
        return Staff.query.all()

    def delete(self, passport_id):
        staff = Staff.query.get(passport_id)
        db.session.delete(staff)
        db.session.commit()
        return Staff.query.all()
