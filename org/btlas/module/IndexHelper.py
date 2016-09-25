__author__ = 'yanglikun'
from git import Repo
from org.btlas.vo.myindex import MyIndex
import jsonpickle
import os


class IndexHelper:
    def __init__(self, workingDir):
        super().__init__()
        self.workingDir = workingDir;

    def getIndex(self):
        repo = Repo(self.workingDir)
        return [MyIndex(entry.hexsha,entry.path) for (path, stage), entry in repo.index.entries.items()]

    def getIndexJSON(self):
        return jsonpickle.encode(self.getIndex(), unpicklable=False)
