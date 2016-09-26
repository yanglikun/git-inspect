__author__ = 'yanglikun'
import jsonpickle


class MyCommit:
    def __init__(self, hash):
        self.tree = None
        self.hash = hash
        self.parents = []
        self.type = 'commit'
        self.msg = ''
        self.author = ''
        self.committer = ''

    def addParent(self, parent):
        self.parent = parent;
