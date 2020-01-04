from flask import Blueprint
from flask_restful import Api

from category.routes import CategoryView

category_bp = Blueprint('category', __name__)
api_category = Api(category_bp)

api_category.add_resource(CategoryView, '/categories')
