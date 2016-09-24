__author__ = 'yanglikun'


class MyBlob:
    def __init__(self, hash):
        super().__init__()
        self.hash = hash
        self.name = ''
        self.content=''
        self.type = 'blob'

    def setName(self, name):
        self.name = name
