from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>Hello, World!</h1>"


@app.route("/<name>")
def hello_user(name):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run(debug=True)