from flask import Flask, request, render_template, jsonify, url_for, session
from werkzeug.utils import secure_filename, redirect
from blueprint.main import vegetable
import os

app = Flask(__name__)

app_list = []

app.config["SECRET_KEY"] = "secret_key_kalika"
app.register_blueprint(vegetable)


@app.route("/", methods=['GET', 'POST'])
def return_info():
    if request.method == 'GET':
        return render_template("hello.html")
    elif request.method == 'POST':
        app_list.append("1")
        return 'OK'
    return 'OK'


@app.route('/request')
def request_object_example():
    data = {
        "request.method": request.method,
        "request.args": request.args,
        "request.headers": request.headers,
        "request.data": request.data
    }
    return 'ok'


@app.route('/save_file', methods=['POST'])
def save_file():
    file = request.files['file']
    path = os.path.join('file', secure_filename(file.filename))
    file.save(path)
    return "ok"


@app.route('/cookies')
def get_cookies():
    cookies = request.cookies
    return jsonify(cookies)


@app.route('/home')
def get_home():
    session["login"] = 'Ok'
    return render_template('main.html')
    # return redirect(url_for('return_info'))


@app.route('/test_session')
def get_session():
    print(session.get('login'))
    app.logger.info("INFO test")
    app.logger.debug("A value for debugging")
    app.logger.warning("A warning occurred (%d apples)", 42)
    app.logger.error("An error occurred")
    return 'Ok session'


@app.errorhandler(404)
def handle_404(error):
    return render_template("error_404.html")


if __name__ == '__main__':
    app.run(debug=True)
