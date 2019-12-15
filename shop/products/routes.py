from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from db import Product
from products.parser import product_parser


class ProductView(Resource):
    @jwt_required
    def get(self):
        return Product.query.all(), 201

    @jwt_required
    def post(self):
        data = request.json
        product_parser.parse_args()
        product = Product(**data)
        product.save_to_db()
        return product.json()

    def patch(self):
        pass

    @jwt_required
    def delete(self, id):
        product = Product.query.get(id)
        if product:
            product.remove_from_db()
            return {
                "message": "Product deleted!"
            }, 200
        return {
            "message": "Product not found!"
        }, 404
