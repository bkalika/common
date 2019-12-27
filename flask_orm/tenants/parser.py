from flask_restful import reqparse

tenant_parser_get = reqparse.RequestParser(bundle_errors=True)
tenant_parser_get.add_argument("passport_id", type=str)
tenant_parser_get.add_argument("name", type=str)
tenant_parser_get.add_argument("age", type=int)
tenant_parser_get.add_argument("sex", type=str)
tenant_parser_get.add_argument("city", type=str)
tenant_parser_get.add_argument("address", type=str)

tenant_parser = reqparse.RequestParser(bundle_errors=True)
tenant_parser.add_argument("passport_id",
                           type=str,
                           required=True,
                           help="Input passport_id")
tenant_parser.add_argument("name",
                           type=str,
                           required=True,
                           help="Input tenant`s name")
tenant_parser.add_argument("age",
                           type=int,
                           required=True,
                           help="Input tenant`s age")
tenant_parser.add_argument("sex",
                           type=str,
                           required=True,
                           choices=["male", "female"],
                           help="Input 'male' or 'female'")
tenant_parser.add_argument("city",
                           type=str,
                           required=True,
                           help="Input tenant`s city")
tenant_parser.add_argument("address",
                           type=str,
                           required=True,
                           help="Input tenant`s city")

tenant_parser_patch = reqparse.RequestParser(bundle_errors=True)
tenant_parser_patch.add_argument("age", type=str)
tenant_parser_patch.add_argument("city", type=str)
tenant_parser_patch.add_argument("address", type=str)
