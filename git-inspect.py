from flask import Flask, request, render_template
import logging
import org.btlas.startFromRepo as startWithRespo



app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route("/getAllCommit", methods=["POST"])
def xf():
    return startWithRespo.getAllCommitJSON(request.form['workingDir'])


if __name__ == '__main__':
    handler = logging.FileHandler(r'flask.log')
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", port=8099,debug=True)
