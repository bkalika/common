from flask_restful import reqparse

staff_parser_get = reqparse.RequestParser(bundle_errors=True)
staff_parser_get.add_argument("passport_id", type=str)
staff_parser_get.add_argument("name", type=str)
staff_parser_get.add_argument("position", type=str)
staff_parser_get.add_argument("salary", type=str)


staff_parser = reqparse.RequestParser(bundle_errors=True)
staff_parser.add_argument("passport_id",
                          type=str,
                          required=True,
                          help="Input passport_id")
staff_parser.add_argument("name",
                          type=str,
                          required=True,
                          help="Input staff name")
staff_parser.add_argument("position",
                          type=str,
                          required=True,
                          help="Input staff position")
staff_parser.add_argument("salary",
                          type=float,
                          required=True,
                          help="Input staff salary")
