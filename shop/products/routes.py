import os
import wave
from xml import parsers

import werkzeug
from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource, abort, marshal_with

from .db import Product
from products.parser import product_parser
from products.structures import product_structure


class ProductView(Resource):
    @marshal_with(product_structure)
    # @jwt_required
    def get(self, id=None):
        if id:
            product = Product.find_product_by_id(id)
            if product:
                return product.json()
            return {"msg": "product id not found!"}
        return Product.query.all(), 201

    @jwt_required
    def post(self):
        data = request.json
        product_parser.parse_args()
        product = Product(data["name"], data["price"], data["category"], data["shop"], data["description"])
        product.save_to_db()
        return product.json()

    @jwt_required
    def patch(self, id):
        file = request.files['file']
        print(id, file)
        path = os.path.join('products/static', file.filename)
        print(path)
        product = Product.query.get(id)
        if product:
            product.image = path
            file.save(path)
            product.save_to_db()
            return {"msg": "Image was uploaded!"}
        abort(404, message="Product id was not found!")

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
