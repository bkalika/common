from flask import Blueprint, Response

tables = Blueprint('tables', __name__)

@tables.route('/tables', methods=['GET'])
def get_tables():
    tables = [{'number': tables.number, 'guest_count': tables.guest_count}]
    return Response(status=200)