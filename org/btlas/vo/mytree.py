__author__ = 'yanglikun'


class MyTree:
    def __init__(self, hash):
        self.subTrees = []
        self.blobs = []
        self.hash = hash
        self.type = 'tree'
        self.name = '/'

    def addSubTree(self, tree):
        self.subTrees.append(tree)

    def addBlob(self, blob):
        self.blobs.append(blob)
        return self;
