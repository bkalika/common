from flask_restful import reqparse, fields, marshal_with

room_structure = {
    "number": fields.Integer,
    "level": fields.Integer,
    "status": fields.String,
    "price": fields.Integer,
}

marshal_with_decor = marshal_with(room_structure)

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("status", type=str, help="Status must be 'Free' or 'Busy'")
