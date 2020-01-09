import os

from flask import Flask

from category import category_bp
from config import get_config
from db import db, migrate
from orders import order_bp
from products import product_bp
from shop_products import shops_products_bp
from shops import shop_bp
from users import user_bp, jwt

env = os.environ.get("ENV")


def create_app(env=env):
    app = Flask(__name__)
    app.config.from_object(get_config(env))
    with app.app_context():
        db.init_app(app)
        jwt.init_app(app)
        db.create_all()
    migrate.init_app(app, db)

    app.register_blueprint(user_bp)
    app.register_blueprint(shop_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(category_bp)
    app.register_blueprint(shops_products_bp)

    return app
