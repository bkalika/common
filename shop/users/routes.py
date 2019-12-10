from flask import request
from flask_restful import Resource, marshal_with
from sqlalchemy.exc import IntegrityError

from db import User, db
from users.parser import user_parser
from users.structure import user_structure


class UserView(Resource):
    method_decorators = [marshal_with(user_structure)]

    def get(self, id=None):
        if id is None:
            args = request.args
            id = args.get("id")
            name = args.get("name")
            email = args.get("email")
            role = args.get("role")
            print(name)
            if id:
                return User.query.filter_by(id=id).all()
            elif name:
                return User.query.filter_by(name=name).all()
            elif email:
                return User.query.filter_by(email=email).all()
            elif role:
                return User.query.filter_by(role=role).all()
            else:
                return User.query.all(), 201
        else:
            return User.query.filter_by(id=id).all(), 201

    def post(self):
        data = request.json
        user_parser.parse_args(strict=True)
        user = User(**data)
        print(user)
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return User.query.all()

    def patch(self, id):
        data = request.json
        user = User.query.get(id)
        user.name = data.get("name")
        user.email = data.get("email")
        user.role = data.get("role")
        db.session.commit()
        return "User updated"

    def delete(self, id):
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return "User deleted"
