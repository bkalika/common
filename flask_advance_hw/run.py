from datetime import timedelta

from flask import Flask, render_template

from products.products import products
from supermarkets.supermarkets import supermarkets

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-super-secret-key'

app.register_blueprint(products)
app.register_blueprint(supermarkets)
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route("/")
@app.route("/home", methods=["GET"])
def get_page_home():
    name = "Home page"
    return render_template("home.html", name=name)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('error_404.html')


if __name__ == "__main__":
    app.run(debug=True)
