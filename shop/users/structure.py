from flask_restful import fields

user_structure = {
    "name": fields.String(40),
    "email": fields.String(70),
    "role": fields.String(20)
}
