from flask import request
from flask_jwt_extended import get_jwt_identity, create_access_token, jwt_required
from flask_restful import Resource

from shops.db import Shop
from shops.parser import shop_parser


class ShopView(Resource):
    @jwt_required
    def get(self):
        return Shop.query.all(), 201

    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        create_access_token(identity=current_user, fresh=False)
        data = request.json
        shop_parser.parse_args(strict=True)
        shop = Shop(**data)
        shop.save_to_db()
        return shop.json()

    @jwt_required
    def patch(self, id):
        shop = Shop.query.get(id)
        if shop:
            data = request.json
            shop.owner = data.get("owner")
            shop.city = data.get("city")
            shop.name = data.get("name")
            shop.save_to_db()
            return shop.json()
        else:
            return {
                "massage": "shop id not found"
            }

    @jwt_required
    def delete(self, id):
        shop = Shop.query.get(id)
        if shop:
            shop.remove_from_db()
            return {
                "message": "Shop deleted!"
            }, 200
        return {
            "message": "Shop not found!"
        }, 404
