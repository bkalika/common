from flask_restful import fields

product_structure = {
    "id": fields.Integer,
    "name": fields.String,
    "price": fields.Integer,
    "category": fields.String,
    "shop": fields.String,
    "description": fields.String,
    "image": fields.String
}