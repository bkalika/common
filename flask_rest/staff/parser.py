from flask_restful import reqparse

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("name", type=str, help="Input name or passport_id")
