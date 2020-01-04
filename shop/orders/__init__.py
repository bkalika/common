from flask import Blueprint
from flask_restful import Api

from orders.routes import OrderView

order_bp = Blueprint('order', __name__)
api_order = Api(order_bp)

api_order.add_resource(OrderView, '/orders')
