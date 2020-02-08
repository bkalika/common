from flask_restful import reqparse

category_parser = reqparse.RequestParser(bundle_errors=True)
category_parser.add_argument("name",
                             type=str,
                             required=True,
                             help="Input category name")
