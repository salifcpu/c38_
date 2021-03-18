from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=["GET", '[POST'])
def index():
    if request.method == "POST":
        name = request.form["username"]
        return render_template("index.html", content="Hello " + name)

    else:
        return render_template("index.html")
