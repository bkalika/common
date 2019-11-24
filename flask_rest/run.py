from flask import Flask, current_app, render_template, Blueprint
from flask_rest.config import Config, run_config
from flask_restful import Api

from flask_rest.rooms import rooms_bp
from flask_rest.staff import staff_bp
from flask_rest.tenants import tenants_bp

app = Flask(__name__)
# app.config.from_object(run_config())
app.config['SECRET_KEY'] = 'my-super-secret-key'
app.config['BUNDLE_ERRORS'] = True
app.register_blueprint(rooms_bp)
app.register_blueprint(tenants_bp)
app.register_blueprint(staff_bp)


if __name__ == "__main__":
    app.run(debug=True)
