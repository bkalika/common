from flask_restful import reqparse

user_parser = reqparse.RequestParser(bundle_errors=True)
user_parser.add_argument("name",
                         type=str,
                         required=True,
                         help="Enter your name. [{error_msg}!]")
user_parser.add_argument("email",
                         type=str,
                         required=True,
                         help="Enter your email. [{error_msg}!]")
user_parser.add_argument("role",
                         type=str,
                         required=True,
                         choices=["Admin", "admin", "Customer", "customer"],
                         help="Who you are? Input 'admin' or 'customer'. [{error_msg}!]")
