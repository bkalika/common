from flask_restful import Resource
from .db import Order


class OrderView(Resource):
    def get(self):
        return Order.query.all(), 201
