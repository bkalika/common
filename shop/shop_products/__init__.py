from flask import Blueprint
from flask_restful import Api

from shop_products.routes import ShopProductView

shops_products_bp = Blueprint('shops_products', __name__)
api_shops_products = Api(shops_products_bp)
api_shops_products.add_resource(ShopProductView, '/shop', '/shop/<int:shop_id>')
