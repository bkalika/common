from flask_restful import Resource

from category.db import Category


class CategoryView(Resource):
    def get(self):
        return Category.query.all(), 201
