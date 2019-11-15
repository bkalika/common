from flask import Flask, render_template
from utils import get_data
from werkzeug.utils import redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def get_home_page():
    return render_template("home.html")


@app.route('/<value>', methods=['GET'])
def get_page(value):
    for product in get_data():
        if product.get('title') == value:
            name = product.get('title')
            data = product.get('text')
            return render_template('main.html', name=name, data=data)
        # else:
        #     # name = product
        #     return error_hangling('main.html')


@app.route("/author", methods=['GET'])
def get_page_author():
    name = "Author:"
    about = "I did it with little looking"
    surname = "Bohdan Kalika"
    return render_template("author.html", name=name, about=about, surname=surname)


if __name__ == "__main__":
    app.run(debug=True)
