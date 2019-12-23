from flask_restful import reqparse

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("name",
                    type=str,
                    help="Input name or passport_id")
parser.add_argument("passport_id",
                    type=str,
                    help="input passport id tenant")
parser.add_argument("age",
                    type=int,
                    choices=[age for age in range(121)],
                    help="Input age from 0 to 120")
parser.add_argument("sex",
                    type=str,
                    choices=["female", "male"],
                    help="input sex 'female' or 'male'")
parser.add_argument("city",
                    type=str,
                    help="input city (str)")
parser.add_argument("street",
                    type=str,
                    help="input street (str)")
parser.add_argument("room_number",
                    type=int,
                    choices=[num for num in range(1, 101)],
                    help="input room number from 1 to 100")
