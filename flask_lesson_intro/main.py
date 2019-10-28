from flask import Flask, render_template
from utils import get_data

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def get_home_page():
    return render_template("home.html", data=get_data())


@app.route("/alarm_clock", methods=['GET', 'POST'])
def get_page_alarm_clock():
    name = "Alarm clock"
    return render_template("alarm_clock.html", data=get_data()[0].values(), name=name)


@app.route("/headphones", methods=['GET', 'POST'])
def get_page_headphones():
    name = "Headphones"
    return render_template("headphones.html", data=get_data()[1].values(), name=name)


@app.route("/IPod", methods=['GET', 'POST'])
def get_ipod():
    name = "iPod"
    return render_template("IPod.html", data=get_data()[2].values(), name=name)


@app.route("/calculator", methods=['GET', 'POST'])
def get_calculator():
    name = "Calculator"
    return render_template("calculator.html", data=get_data()[3].values(), name=name)


@app.route("/coffeemaker", methods=['GET', 'POST'])
def get_coffeemaker():
    name = "Coffeemaker"
    return render_template("coffeemaker.html", data=get_data()[4].values(), name=name)


@app.route("/battery_charger", methods=['GET', 'POST'])
def get_battery_charger():
    name = "Battery charger"
    return render_template("battery_charger.html", data=get_data()[5].values(), name=name)


@app.route("/author", methods=['GET', 'POST'])
def get_page_author():
    name = "Author:"
    about = "I did it with little looking"
    surname = "Bohdan Kalika"
    return render_template("author.html", name=name, about=about, surname=surname)


if __name__ == "__main__":
    app.run(debug=True)
