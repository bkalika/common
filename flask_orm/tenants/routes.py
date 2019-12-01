from flask import request
from flask_restful import Resource, marshal_with
from sqlalchemy.exc import IntegrityError

from db import Tenant, db
from tenants.structures import tenant_structure


class Tenants(Resource):
    method_decorators = [marshal_with(tenant_structure)]

    def get(self, passport_id=None):
        if passport_id is None:
            args = request.args
            passport_id = args.get("passport_id")
            name = args.get("name")
            age = args.get("age")
            sex = args.get("sex")
            city = args.get("city")
            address = args.get("address")
            if passport_id:
                return Tenant.query.filter_by(passport_id=passport_id).all()
            elif name:
                return Tenant.query.filter_by(name=name).all()
            elif age:
                return Tenant.query.filter_by(age=age).all()
            elif sex:
                return Tenant.query.filter_by(sex=sex).all()
            elif city:
                return Tenant.query.filter_by(city=city).all()
            elif address:
                return Tenant.query.filter_by(address=address).all()
        else:
            return Tenant.query.filter_by(passport_id=passport_id).all(), 201
        return Tenant.query.all(), 201

    def post(self):
        data = request.json
        tenant = Tenant(**data)
        try:
            db.session.add(tenant)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return Tenant.query.all()

    def patch(self, passport_id):
        data = request.json
        tenant = Tenant.query.get(passport_id)
        tenant.age = data.get("age")
        tenant.city = data.get("city")
        tenant.address = data.get("address")
        db.session.commit()
        return Tenant.query.all()

    def delete(self, passport_id):
        tenant = Tenant.query.get(passport_id)
        db.session.delete(tenant)
        db.session.commit()
        return Tenant.query.all()
