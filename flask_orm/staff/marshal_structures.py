from flask_restful import fields

room_structure = {
    "passport_id": fields.String,
    "name": fields.String,
    "position": fields.String(40),
    "salary": fields.Float
}
