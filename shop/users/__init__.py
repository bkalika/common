from flask import Blueprint
from flask_restful import Api

from users.routes import UserView

user_bp = Blueprint('user', __name__)
api_user = Api(user_bp)

api_user.add_resource(UserView, '/users', '/users/<int:id>')
