from flask_restful import reqparse

shop_parser = reqparse.RequestParser(bundle_errors=True)
shop_parser.add_argument("name",
                         type=str,
                         required=True,
                         help="Enter shop name. [{error_msg}]!")
shop_parser.add_argument("city",
                         type=str,
                         required=True,
                         help="Enter shop location. [{error_msg}!]")
shop_parser.add_argument("owner",
                         type=str,
                         required=True,
                         help="Enter shop owner! [{error_msg}!]")
