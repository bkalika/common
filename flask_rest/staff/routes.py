import json

from flask import request
from flask_restful import Resource

from staff.models import Staff
from staff.parser import parser
from utils import read_data, write_data

json_file = 'staff/staff.json'
json_data = read_data(json_file)
staff_data = json.load(open(json_file))


class StaffView(Resource):
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
            else:
                return "404 staff not found"

    def post(self):
        data = request.json
        parser.parse_args(strict=True)
        for staff in json_data:
            if staff.get("passport_id") == data["passport_id"]:
                return "Staff already works"
        else:
            staff_data.append(Staff(
                data["name"],
                data["passport_id"],
                data["position"],
                data["salary"],
            ).to_dict())
            write_data(staff_data, json_file)
            return "Staff hired"

    def patch(self):
        data = request.json
        for staff in staff_data:
            if staff.get("name") == data.get("name"):
                staff.update(data)
        write_data(staff_data, json_file)
        return "Staff updated"

    def delete(self):
        data = request.json
        for staff in range(len(staff_data)):
            if staff_data[staff].get("name") == data.get("name"):
                del staff_data[staff]
                break
        else:
            return "Staff does not work"
        write_data(staff_data, json_file)
        return "Staff dismissed"
