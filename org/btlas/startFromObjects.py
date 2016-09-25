__author__ = 'yanglikun'
from git import Repo
import jsonpickle
from git.objects.commit import Commit
from git.objects.blob import Blob
from gitdb.util import hex_to_bin

from  org.btlas.vo.categoryObjects import CategoryObjects
from org.btlas.vo.mycommit import MyCommit
from org.btlas.vo.mytree import MyTree
from org.btlas.vo.myblob import MyBlob
from org.btlas.vo.myauthor import MyAuthor
from org.btlas.vo.mycommitter import MyCommitter


def createTree(repo, shaBin, shaStr):
    output = repo.git.execute('git cat-file -p ' + shaStr);
    myTree = MyTree(shaStr)
    for line in output.split("\n"):
        fields = line.split(' ')
        type = fields[1]
        hashAndNameArr = fields[2].split('\t')
        hash = hashAndNameArr[0]
        name = hashAndNameArr[1]
        if type == 'tree':
            mySubTree = MyTree(hash)
            mySubTree.name = name
            myTree.addSubTree(mySubTree)
        elif type == 'blob':
            mySubBlob = MyBlob(hash)
            mySubBlob.name = name
            myTree.addBlob(mySubBlob)
    return myTree


def createCommit(repo, shaBin, shaStr):
    comm = Commit(repo, shaBin)
    myCommit = MyCommit(shaStr)
    myCommit.author = MyAuthor(comm.author.name, comm.author.email);
    myCommit.committer = MyCommitter(comm.committer.name, comm.committer.email);
    myCommit.msg = comm.message
    myCommit.tree = comm.tree.hexsha
    if comm.parents:
        myCommit.parents = [pcommit.hexsha for pcommit in comm.parents]

    return myCommit;


def createBlob(repo, shaBin, shaStr):
    blob = Blob(repo, shaBin)
    myBlob = MyBlob(shaStr);
    try:
        myBlob.content = blob.data_stream.read().decode('utf-8');
    except:
        print(shaStr)
    return myBlob;


def getCategoryObjects(workingDir):
    repo = Repo(workingDir)
    co = CategoryObjects();

    allShaWithName = repo.git.execute('git rev-list --objects --all --indexed-objects');
    allSha = [item.split(' ')[0] for item in allShaWithName.split('\n') if item]
    for shaStr in allSha:
        shaBin = hex_to_bin(shaStr);
        info = repo.odb.info(shaBin)
        type = info.type.decode('utf-8')
        if type == 'tree':
            co.trees.append(createTree(repo, shaBin, shaStr))
        elif type == 'commit':
            co.commits.append(createCommit(repo, shaBin, shaStr))
        elif type == 'blob':
            co.blobs.append(createBlob(repo, shaBin, shaStr))
        else:
            pass
    return co;


def getCategoryObjectsJson(workingDir):
    categoryObjects = getCategoryObjects(workingDir);
    return jsonpickle.encode(categoryObjects, unpicklable=False)


if __name__ == '__main__':
    import time

    begin = time.time();
    categoryObjects = getCategoryObjects(r'd:/worksapce/git/git-test');
    print(jsonpickle.encode(categoryObjects, unpicklable=False))
    print(time.time() - begin)
