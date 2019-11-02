from flask import Flask, request, render_template

app = Flask(__name__)

app_list = []

@app.route("/", methods=['GET', 'POST'])
def return_info():
    if request.method == 'GET':
        return render_template("hello.html")
    elif request.method == 'POST':
        app_list.append("1")
        print(app_list)
        return 'OK'
    return 'ok'


@app.route('/request')
def request_object_example():
    data = {
        "request.method": request.method,
        "request.args": request.args,
        "request.headers": request.headers,
        "request.data": request.data
    }
    print(data)
    return 'ok'

@app.route('/save_file', methods=['POST'])
def save_file():
    file = request.files
    return

@app.route('/home')
def get_home():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
