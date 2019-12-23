import os

from flask import Flask, current_app
from config import get_config

from rooms import rooms_bp
from staff import staff_bp
from tenants import tenants_bp

env = os.environ.get("ENV")
app = Flask(__name__)
app.config.from_object(get_config(env=env))
app.register_blueprint(rooms_bp)
app.register_blueprint(tenants_bp)
app.register_blueprint(staff_bp)

# for checking secret_key:
@app.route("/")
def hello():
    return current_app.config["SECRET_KEY"]


if __name__ == "__main__":
    app.run()
