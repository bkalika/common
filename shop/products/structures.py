from flask_restful import fields

product_structure = {
    "id": fields.Integer,
    "name": fields.String,
    "price": fields.Float,
    "category": fields.Integer,
    "description": fields.String,
    "image": fields.String
}