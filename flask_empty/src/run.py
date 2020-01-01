from flask import Response, Flask

from infrastructure import DB
# from src import tables
# from src import restaurant
from src.routes.restaurant import restaurant
from src.routes.tables import tables


def setup_db():
    DB['restaurant'] = []
    DB['tables'] = []


def create_app():
    setup_db()
    app = Flask(__name__, instance_relative_config=False)
    with app.app_context():
        app.register_blueprint(restaurant)
        app.register_blueprint(tables)
        return app


app = create_app()


@app.route('/_health_check', methods=['GET'])
def check():
    response = Response(status=200)
    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
