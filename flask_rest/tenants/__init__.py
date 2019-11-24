from flask import Blueprint
from flask_restful import Api

from flask_rest.tenants.tenants import Tenants

tenants_bp = Blueprint('tenants', __name__)
app = Api(tenants_bp)
app.add_resource(Tenants, '/tenants', '/tenants/<string:name>')
