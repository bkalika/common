from flask_restful import fields

user_structure = {
    "name": fields.String(default='user`s id not found'),
    "email": fields.String(default="email not found"),
    "password": fields.String(default='Incorrect id'),
    "role": fields.String(default="incorrect id"),
}


shop_structure = {
    "owner": fields.String,
    "city": fields.String,
    "name": fields.String
}