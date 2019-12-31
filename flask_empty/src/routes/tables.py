from flask import Blueprint



tables = Blueprint('tables', __name__)

@tables.route('/tables', methods=['GET'])
def get_tables():
    tables = [{'number': tables. number, 'guest_count': tables.guest_count}]