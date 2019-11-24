from flask import Flask, current_app
from flask_rest.config import run_config

from flask_rest.rooms import rooms_bp
from flask_rest.staff import staff_bp
from flask_rest.tenants import tenants_bp


app = Flask(__name__)
app.config.from_object(run_config())
app.register_blueprint(rooms_bp)
app.register_blueprint(tenants_bp)
app.register_blueprint(staff_bp)

# for checking secret_key:
@app.route("/")
def hello():
    return current_app.config["SECRET_KEY"]


if __name__ == "__main__":
    app.run()
