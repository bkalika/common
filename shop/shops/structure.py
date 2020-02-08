from flask_restful import fields

shop_structure = {
    "id": fields.Integer,
    "owner": fields.String,
    "city": fields.String,
    "name": fields.String
}
