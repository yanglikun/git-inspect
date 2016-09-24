__author__ = 'yanglikun'
from git import Repo
import jsonpickle
from org.btlas.vo.mycommit import MyCommit
from org.btlas.vo.mytree import MyTree
from org.btlas.vo.myblob import MyBlob
from org.btlas.vo.myauthor import MyAuthor
from org.btlas.vo.mycommitter import MyCommitter


def buildMyCommit(item):
    myCommit = MyCommit(item.hexsha)
    myCommit.author=MyAuthor(item.author.name, item.author.email);
    myCommit.committer=MyCommitter(item.committer.name,item.committer.email);

    myCommit.msg = item.message
    if item.parents:
        myCommit.parents = [pcommit.hexsha for pcommit in item.parents]

    myCommit.tree = buildMyTrees(item.tree);
    return myCommit;


def buildMyTrees(tree):
    myTree = MyTree(tree.hexsha)
    if tree.name:
        myTree.name = tree.name

    myTree.blobs = buildMyBlobs(tree);

    subTrees = tree.trees;
    if subTrees:
        for subTree in subTrees:
            myTree.addSubTree(buildMyTrees(subTree));

    return myTree;


def buildMyBlobs(tree):
    myBlobs = []
    for bloblItem in tree.blobs:
        myBlob = MyBlob(bloblItem.hexsha);
        myBlob.name = bloblItem.name
        myBlob.content = bloblItem.data_stream.read().decode('utf-8')
        myBlobs.append(myBlob);
    return myBlobs;


repo = Repo(r'D:\worksapce\git\git-test')

myCommits=[]

for item in repo.iter_commits():
    myCommits.append(buildMyCommit(item))

print(jsonpickle.encode(myCommits,unpicklable=False))