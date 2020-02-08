import hashlib
from flask import request
from flask_jwt_extended import (create_access_token, create_refresh_token, get_jwt_identity, jwt_refresh_token_required)
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from db import db
from users.db import User
from users.parser import user_parser


class UserView(Resource):
    def get(self, id):
        user = User.find_user_by_id(id)
        print(user)
        if user:
            return user.json()
        return {
            "message": "User not found!"
        }, 404

    def patch(self, id):
        user = User.query.get(id)
        if user:
            data = request.json
            user.name = data.get("name")
            user.email = data.get("email")
            user.password = hashlib.sha256(data["password"].encode("utf-8")).hexdigest()
            user.role = data.get("role")
            db.session.commit()
            return user.json()
        return {"message": "User not found"}

    def delete(self, id):
        user = User.query.get(id)
        if user:
            user = User.query.get(id)
            db.session.delete(user)
            db.session.commit()
            return {"message": f"User with name {user.name} deleted"}, 200
        return {"message": "User not found"}, 404


class UserRegister(Resource):
    def post(self):
        data = request.json
        user_parser.parse_args(strict=True)
        check_email = db.session.query(User.email).filter(User.email == data.get("email")).all()
        if check_email:
            return {"message": f"User with email {check_email} already exist"}, 400
        user = User(data["name"],
                    data["email"],
                    hashlib.sha256(data["password"].encode("utf-8")).hexdigest(),
                    data["role"])
        try:
            db.session.add(user)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
        return user.json()


class UserLogin(Resource):
    def post(self):
        data = request.json
        authorization = User.query.filter_by(email=data["email"]).first()
        if authorization.email and authorization.password == hashlib.sha256(data["password"].encode("utf-8")).hexdigest():
            access_token = create_access_token(identity=authorization.id, fresh=True)  # Puts User ID as Identity in JWT
            refresh_token = create_refresh_token(identity=authorization.id)  # Puts User ID as Identity in JWT
            return {
                "access_token": access_token,
                "refresh_token": refresh_token
            }, 200
        return {
            "message": "Invalid credentials"
        }, 401


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user_id = get_jwt_identity()  # Gets Identity from JWT
        new_token = create_access_token(identity=current_user_id, fresh=False)
        return {
            "access_token": new_token
        }, 200
