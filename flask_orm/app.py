from flask import Flask
from datetime import timedelta

from flask_orm.config import run_config
from flask_orm.db import db, migrate
from flask_orm.rooms import rooms_bp
from flask_orm.tenants import tenants_bp
# from flask_orm.staff import staff_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(run_config())

    db.init_app(app=app)
    db.create_all()
    migrate.init(app, db)
    app.permanent_session_lifetime = timedelta(minutes=20)

    app.register_blueprint(rooms_bp)
    app.register_blueprint(tenants_bp)
    # app.register_blueprint(staff_bp)

    return app
