from flask_restful import fields

room_structure = {
    "id": fields.Integer,
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String(40),
    "price": fields.Integer
}
