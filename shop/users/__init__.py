from flask import Blueprint, jsonify
from flask_jwt_extended import JWTManager, jwt_required
from flask_restful import Api

from users.routes import UserView, UserRegister, UserLogin

user_bp = Blueprint('user', __name__)
api_user = Api(user_bp)
jwt = JWTManager()
# @jwt_required


@jwt.expired_token_loader
def expired_token_callback():
    return jsonify(
        {
            "description": "Token has expired!",
            "error": "token_expired"
        }, 401
    )


@jwt.invalid_token_loader
def invalid_token_callback():
    return jsonify(
        {
            "description": "Signature verification failed!",
            "error": "invalid_token"
        }, 401
    )


@jwt.unauthorized_loader
def unauthorized_loader_callback(error):
    return jsonify(
        {
            "description": "Access token not found!",
            "error": "unauthorized_loader"
        }, 401
    )


@jwt.needs_fresh_token_loader
def fresh_token_loader_callback():
    return jsonify(
        {
            "description": "Token is not fresh. Fresh token needed!",
            "error": "needs_fresh_token"
        }, 401
    )


api_user.add_resource(UserView, '/users/<int:id>')
api_user.add_resource(UserRegister, '/register')
api_user.add_resource(UserLogin, '/login')
