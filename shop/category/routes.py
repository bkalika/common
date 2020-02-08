from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource, marshal_with

from category.db import Category
from category.parser import category_parser
from category.structures import category_structure
from db import db


class CategoryView(Resource):
    # @jwt_required
    @marshal_with(category_structure)
    def get(self):
        return Category.query.all(), 201

    # @jwt_required
    def post(self):
        data = request.json
        category_parser.parse_args(strict=True)
        check_category = db.session.query(Category.name).filter(Category.name == data.get('name')).all()
        if check_category:
            return {"message": f'Category {check_category} already exist!'}, 400
        category = Category(**data)
        category.save_to_db()
        return category.json()

    @jwt_required
    def patch(self, id):
        category = Category.query.get(id)
        if category:
            data = request.json
            category.name = data.get('name')
            category.save_to_db()
            return category.json()
        else:
            return {
                "message": "Category id not found!"
            }

    @jwt_required
    def delete(self, id):
        category = Category.query.get(id)
        if category:
            category.remove_from_db()
            return {
                "message": "Category deleted!"
            }, 200
        return {
            "message": "Category not found!"
        }, 404
