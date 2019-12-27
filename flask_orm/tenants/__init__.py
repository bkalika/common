from flask import Blueprint
from flask_restful import Api

from tenants.routes import Tenants

tenants_bp = Blueprint("tenants", __name__)

api_tenants = Api(tenants_bp)
api_tenants.add_resource(Tenants, '/tenants', '/tenants/<string:passport_id>')
