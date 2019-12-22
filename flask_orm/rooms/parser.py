from flask_restful import reqparse

room_parser_get = reqparse.RequestParser(bundle_errors=True)
room_parser_get.add_argument("number", type=int)
room_parser_get.add_argument("level", type=int)
room_parser_get.add_argument("status", type=str)
room_parser_get.add_argument("price", type=int)

room_parser = reqparse.RequestParser(bundle_errors=True)
room_parser.add_argument("number",
                         type=int,
                         help="Input room number that is greater 0 and less 101. Important: {error_msg}!!!")
room_parser.add_argument("level",
                         type=int,
                         choices=[num for num in range(1, 10)],
                         required=True,
                         help="Input level that is greater than 0 and less than 11")
room_parser.add_argument("status",
                         type=str,
                         choices=["Free", "Busy"],
                         required=True,
                         help="Status must be 'Free' or 'Busy'")
room_parser.add_argument("price",
                         type=int,
                         choices=[num for num in range(1, 1001)],
                         required=True,
                         help="Price per room must be from 1$-1000$ (integer)")

room_status_parser = reqparse.RequestParser(bundle_errors=True)
room_status_parser.add_argument("status",
                                type=str,
                                choices=['Free', 'Busy'],
                                help="Status must be 'Free' or 'Busy'")
room_status_parser.add_argument("tenant_id",
                                type=str,
                                help="Input passport_id")

room_staff_parser_get = reqparse.RequestParser(bundle_errors=True)
room_staff_parser_get.add_argument("number", type=int)
room_staff_parser_get.add_argument("passport_id", type=str)
