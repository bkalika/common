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
        image = request.files['image']
        product.save_to_db()
        return product.json()

# class UploadWavAPI(Resource):
#     def post(self):
#     args = parse.parse_args()
#     stream = args['audio'].stream wav_file = wave.open(stream, 'rb')
#     signal = wav_file.readframes(-1) signal = np.fromstring(signal, 'Int16')
#     fs = wav_file.getframerate() wav_file.close()




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
