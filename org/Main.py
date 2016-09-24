from flask import Flask, request, render_template
import logging
import json



app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/xf", methods=["POST"])
def xf():
    return render_template("suc.html")


@app.route("/queryPage")
def queryPage():
    return render_template("query.html")

@app.route("/query", methods=["POST"])
def query():
    pass

@app.route("/no")
def no():
    return render_template("no.html")

if __name__ == '__main__':
    handler = logging.FileHandler(r'flask.log')
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", port=4321)
