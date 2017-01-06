from flask import Flask, request, render_template
import logging
import org.btlas.startFromRepo as startWithRespo
from org.btlas.module.indexHelper import IndexHelper
from git.exc import NoSuchPathError, InvalidGitRepositoryError
import jsonpickle

app = Flask(__name__, static_url_path='')


@app.route('/')
def home():
    return app.send_static_file('index.html')


@app.route("/allCommit", methods=["POST"])
def allCommit():
    return startWithRespo.getAllCommitJSON(request.form['workingDir'])


@app.route("/index", methods=["POST"])
def index():
    try:
        indexHelper = IndexHelper(request.form['workingDir'])
        return indexHelper.getIndexJSON()
    except NoSuchPathError as e:
        return jsonpickle.encode({"suc":False,"msg":"路径不存在:"+str(e)}, unpicklable=False)
    except InvalidGitRepositoryError as e:
        return jsonpickle.encode({"suc":False,"msg":"路径不是git仓库:"+str(e)}, unpicklable=False)
    except Exception as e:
        return jsonpickle.encode({"suc":False,"msg":"系统异常:"+str(e)}, unpicklable=False)


@app.route("/categoryObjects", methods=["POST"])
def categoryObjects():
    try:
        from org.btlas.startFromObjects import getCategoryObjectsJson
        return getCategoryObjectsJson(request.form['workingDir'])
    except NoSuchPathError as e:
        return jsonpickle.encode({"suc":False,"msg":"路径不存在:"+str(e)}, unpicklable=False)
    except InvalidGitRepositoryError as e:
        return jsonpickle.encode({"suc":False,"msg":"路径不是git仓库:"+str(e)}, unpicklable=False)
    except Exception as e:
        return jsonpickle.encode({"suc":False,"msg":"系统异常:"+str(e)}, unpicklable=False)


if __name__ == '__main__':
    handler = logging.FileHandler(r'flask.log')
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", port=8099, debug=True)
