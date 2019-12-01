from flask import Flask
from datetime import timedelta

from config import get_config
from db import db, migrate
from rooms import rooms_bp
from tenants import tenants_bp
from staff import staff_bp


def create_app(env="TEST"):
    app = Flask(__name__)
    app.config.from_object(get_config(env))
    with app.app_context():
        db.init_app(app)
        db.create_all()
    migrate.init_app(app, db)
    app.permanent_session_lifetime = timedelta(minutes=20)

    app.register_blueprint(rooms_bp)
    app.register_blueprint(tenants_bp)
    app.register_blueprint(staff_bp)

    return app
