from flask_restful import reqparse

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("name",
                    type=str,
                    help="Input name(str)")
parser.add_argument("passport_id",
                    type=str,
                    help="input passport id(str)")
parser.add_argument("position",
                    type=str,
                    help="input position(str)")
parser.add_argument("salary",
                    type=int,
                    choices=[salary for salary in range(1, 2001)],
                    help="Input salary for staff in range 1$ and 2000$ (int)")

