from flask_restful import fields

products_in_shop = {
    "id": fields.Integer,
    "name": fields.String,
    "price": fields.Integer,
    "category": fields.Integer,
    "description": fields.String,
    "image": fields.String
}
