from flask_restful import fields

room_structure = {
    "passport_id": fields.String(8),
    "name": fields.String(40),
    "age": fields.Integer,
    "sex": fields.String(10),
    "city": fields.String(100),
    "address": fields.String(100)
}
