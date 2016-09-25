from flask import Flask, request, render_template
import logging
import org.btlas.startFromRepo as startWithRespo
from org.btlas.module.indexHelper import IndexHelper

app = Flask(__name__,static_url_path='')


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route("/allCommit", methods=["POST"])
def allCommit():
    return startWithRespo.getAllCommitJSON(request.form['workingDir'])


@app.route("/index", methods=["POST"])
def index():
    indexHelper = IndexHelper(r'D:\worksapce\git\git-test')
    return indexHelper.getIndexJSON()


@app.route("/categoryObjects", methods=["POST"])
def categoryObjects():
    from org.btlas.startFromObjects import getCategoryObjectsJson
    return getCategoryObjectsJson(request.form['workingDir'])


if __name__ == '__main__':
    handler = logging.FileHandler(r'flask.log')
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", port=8099, debug=True)
