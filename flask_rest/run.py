from flask import Flask, current_app, render_template, Blueprint
from flask_rest.config import Config, run_config
from flask_restful import Api

from flask_rest.rooms import rooms_bp

app = Flask(__name__)
# app.config.from_object(run_config())
app.config['SECRET_KEY'] = 'my-super-secret-key'
app.config['BUNDLE_ERRORS'] = True
app.register_blueprint(rooms_bp)


@app.route('/')
def home():
    # return current_app.config["SECRET_KEY"]
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
