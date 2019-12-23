from flask_restful import reqparse

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument("number",
                    type=int,
                    choices=[num for num in range(1, 101)],
                    help="Input room number that is greater than 0 and less than 101")
parser.add_argument("level",
                    type=int,
                    choices=[num for num in range(1, 10)],
                    help="Input level that is greater than 0 and less than 11")
parser.add_argument("status",
                    type=str,
                    choices=["Free", "Busy"],
                    help="Status must be 'Free' or 'Busy'")
parser.add_argument("price",
                    type=int,
                    choices=[num for num in range(1, 1001)],
                    help="Price per room must be from 1$-1000$ (integer)")
