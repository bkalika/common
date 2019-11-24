from flask import Blueprint
from flask_restful import Api

from flask_rest.staff.staff import Staff

staff_bp = Blueprint('staff', __name__)
api = Api(staff_bp)
api.add_resource(Staff, '/staff', '/staff/<string:name>')
