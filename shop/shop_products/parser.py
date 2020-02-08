from flask_restful import reqparse

shop_product_parser = reqparse.RequestParser(bundle_errors=True)
shop_product_parser.add_argument("product_id",
                                 required=True,
                                 help="Input product id")
shop_product_parser.add_argument("amount",
                                 required=True,
                                 help="Input products amount")
