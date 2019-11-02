from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route("/<value>", methods=['GET'])
def get_page_iwatch(value):
    print(value)
    return render_template("iwatch.html", data=get_data()[0])


# @app.route("/headphones", methods=['GET'])
# def get_page_headphones():
#     return render_template("headphones.html", data=get_data()[1])
#
#
# @app.route("/IPod", methods=['GET'])
# def get_page_ipod():
#     return render_template("IPod.html", data=get_data()[2])
#
#
# @app.route("/calculator", methods=['GET'])
# def get_page_calculator():
#     return render_template("calculator.html", data=get_data()[3])
#
#
# @app.route("/coffeemaker", methods=['GET'])
# def get_page_coffeemaker():
#     return render_template("coffeemaker.html", data=get_data()[4])
#
#
# @app.route("/battery_charger", methods=['GET'])
# def get_page_battery_charger():
#     return render_template("battery_charger.html", data=get_data()[5])
#
#
# @app.route("/author", methods=['GET'])
# def get_page_author():
#     name = "Author:"
#     about = "I did it with little looking"
#     surname = "Bohdan Kalika"
#     return render_template("author.html", name=name, about=about, surname=surname)


if __name__ == "__main__":
    app.run(debug=True)
