from flask_restful import fields

room_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String(40),
    "price": fields.Float
}
