from flask import Blueprint
from flask_restful import Api

from flask_rest.staff.staff import StaffView

staff_bp = Blueprint('staff', __name__)
api = Api(staff_bp)
api.add_resource(StaffView, '/staff', '/staff/<string:name>')
