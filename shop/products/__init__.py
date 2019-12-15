from flask import Blueprint
from flask_restful import Api

from products.routes import ProductView

product_bp = Blueprint('product', __name__)
api_product = Api(product_bp)

api_product.add_resource(ProductView, '/products', '/products/<int:id>')
