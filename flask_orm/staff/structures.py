from flask_restful import fields

staff_structure = {
    "passport_id": fields.String(8),
    "name": fields.String(40),
    "position": fields.String(40),
    "salary": fields.Float
}
