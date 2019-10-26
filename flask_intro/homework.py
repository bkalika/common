from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home')
def home_func():
    return render_template("home.html")


@app.route('/vegetables', methods=['GET', 'POST'])
def vegetables_func():
    vegetables_list = ["beans", "carrot", "beetroot", "cucumber"]
    return render_template("vegetables.html", list=vegetables_list)


@app.route('/fruits', methods=['GET', 'POST'])
def fruits_func():
    fruits_list = ["melon", "apple", "strawberry", "grape"]
    return render_template("fruits.html", list=fruits_list)


if __name__ == "__main__":
    app.run(debug=True)
