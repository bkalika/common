from flask_restful import Resource


class Tenants(Resource):
    def get(self):
        return "get"

    def post(self):
        return "post"

    def patch(self):
        return "patch"

    def put(self):
        return "put"

    def delete(self):
        return "delete"
