import werkzeug
from flask_restful import reqparse

product_parser = reqparse.RequestParser(bundle_errors=True)
product_parser.add_argument("name",
                            type=str,
                            required=True,
                            help="Input product name")
product_parser.add_argument("price",
                            type=float,
                            required=True,
                            help="Input product price")
product_parser.add_argument("category",
                            type=str,
                            required=True,
                            help="Input product category")
product_parser.add_argument("shop",
                            type=str,
                            required=True,
                            help="Input shop, whe this product is selling")
product_parser.add_argument("description",
                            type=str,
                            required=True,
                            help="Input product description")
product_parser.add_argument("image",
                            type=werkzeug.FileStorage,
                            required=False,
                            location='files',
                            help="Input path for product image")
