from flask import Flask
from markupsafe import escape
app =Flask(__name__)


@app.route("/")
def home1():
    return "Wellcome"

@app.route("/<name>")
def hello(name):
    return f"hello, {escape(name)}!"

@app.route("/home")
def home():
    return "HOME PAGE"

if __name__ == '__main__':
    app.run()
    