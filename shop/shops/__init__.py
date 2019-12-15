from flask import Blueprint
from flask_restful import Api

from shops.routes import ShopView

shop_bp = Blueprint('shop', __name__)
api_shop = Api(shop_bp)

api_shop.add_resource(ShopView, '/shops', '/shops/<int:id>')
