from datetime import timedelta

from flask import Flask, current_app

from flask_orm.config import run_config
from flask_orm.db import db
from flask_orm.rooms import rooms_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app)
    app.permanent_session_lifetime = timedelta(minutes=20)  # add session expire dat

    app.register_blueprint(rooms_bp)

    return app


if __name__ == "__main__":
    create_app().run()
