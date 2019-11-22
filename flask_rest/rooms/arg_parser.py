from flask_restful import reqparse, fields, marshal_with

room_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Integer,
}

marshal_with_decor = marshal_with(room_structure)

# parser = reqparse.RequestParser(bundle_errors=True)
# parser.add_argument("number", type=int, required=True, help="Number must be integer")
# parser.add_argument("level", type=int, required=True, help="Level must be integer")
# parser.add_argument("status", type=str, required=True, help="Status must be 'Free' or 'Busy'")
# parser.add_argument("price", type=str, required=True, help="Price myst be int and >= 0")

# parser = reqparse.RequestParser(bundle_errors=True)
# parser.add_argument("number", type=int, location='args')
# parser.add_argument("level", type=int, location='args')
# parser.add_argument("status", type=str, location='args')
# parser.add_argument("price", type=int, location='args')

# parser_post = parser.copy()
# parser_post.replace_argument("number",
#                              type=int,
#                              location="form",
#                              required=True,
#                              help="Number must be integer")
# parser_post.replace_argument("level",
#                              type=int,
#                              location="form",
#                              required=True,
#                              help="Level must be integer")
# parser_post.replace_argument("status",
#                              type=str,
#                              location="form",
#                              required=True,
#                              help="Status must be 'Free' or 'Busy'")
# parser_post.replace_argument("price",
#                              type=int,
#                              location="form",
#                              required=True,
#                              help="Price must be int and >= 0")
