import json

from flask import request
from flask_restful import Resource

from flask_rest.staff.parser import parser
from flask_rest.utils import read_data, write_data

json_file = 'staff/staff.json'
json_data = read_data(json_file)
staff_data = json.load(open(json_file))


class Staff(Resource):
    def get(self, name=None):
        if name is None:
            args = parser.parse_args(strict=True)
            if args.name is not None:
                info_staff = []
                for staff in json_data:
                    if staff.get("name") == args.get("name") or staff.get("passport_id") == args.get("passport_id"):
                        info_staff.append(staff)
                return info_staff
            else:
                return json_data
        elif name:
            for staff in json_data:
                if staff.get("name") == name or staff.get("passport_id") == name:
                    return staff

    def post(self):
        data = request.json
        staff_data.append(Staff(
            data["name"],
            data["passport_id"],
            data["position"],
            data["salary"],
        ).to_dict())
        write_data(staff_data, json_file)
        return "Staff hired"
