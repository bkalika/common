from flask_restful import fields

user_structure = {
    "name": fields.String(40),
    "email": fields.String(70),
    "password": fields.String(),
    "role": fields.String(20)
}
