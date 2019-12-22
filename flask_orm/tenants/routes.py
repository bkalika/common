from flask import request
from flask_restful import Resource, marshal_with, abort
from sqlalchemy.exc import IntegrityError

from db import Tenant, db
from tenants.parser import tenant_parser_get, tenant_parser, tenant_parser_patch
from tenants.structures import tenant_structure


class Tenants(Resource):
    @marshal_with(tenant_structure)
    def get(self, passport_id=None):
        data = tenant_parser_get.parse_args()
        if passport_id:
            return Tenant.query.filter_by(passport_id=passport_id).first_or_404()
        elif any(tuple(data.values())):
            return Tenant.query.filter_by(**{k: v
                                             for k, v in data.items()
                                             if v}).all(), 200
        return Tenant.query.all(), 200

    def post(self):
        data = tenant_parser.parse_args()
        if not Tenant.query.filter_by(passport_id=data["passport_id"]).scalar():
            try:
                db.session.add(Tenant(**data))
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
            return {"msg": "Tenant was added!"}
        abort(404, message="Tenant already exist!")

    def patch(self, passport_id):
        data = tenant_parser_patch.parse_args()
        tenant = Tenant.query.get(passport_id)
        print(tenant_parser_patch)
        if tenant:
            tenant.age = data["age"]
            tenant.city = data["city"]
            tenant.address = data["address"]
            db.session.commit()
            return {"msg": f"Tenant {passport_id} was updated!"}
        abort(404, message="Tenant not found!")

    def delete(self, passport_id):
        if Tenant.query.filter_by(passport_id=passport_id).scalar():
            tenant = Tenant.query.get(passport_id)
            db.session.delete(tenant)
            db.session.commit()
            return {"message": f"Tenant {passport_id} was deleted!"}
        abort(404, message=f"Tenant {passport_id} not found!")
