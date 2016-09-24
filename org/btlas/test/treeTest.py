__author__ = 'yanglikun'
from git import Repo
from gitdb.util import bin_to_hex
import os
from git.objects.commit import Commit
from git.objects.blob import Blob
from git.objects.tree import Tree

repo = Repo(r'D:\worksapce\git\git-test')
#
# for item in repo.odb.sha_iter():
#     info = repo.odb.info(item);
#     shaBin = info.binsha
#     sharStr=info.hexsha.decode('ascii')
#     type = info.type
#     typeStr = type.decode('ascii')
#     if typeStr == 'tree':
#         tree = Tree(repo, shaBin)
#         print(info.binsha,":",sharStr)


tree=Tree(repo, b'Imd(\xb9\xcf\x92\x98\x1d\xc9IR\x11\xe6\xe1\x12\x0f\xb6\xf2\xba')
print(tree.hexsha)


# print("--------------")
# comm = Commit(repo, b'\x07$\xe5\x92f\xcb]\x97\xd4\xe9s\x9c\xaf\xa0b\xfb\n1\xa1\x95')
# print(comm.message)
# print(comm.hexsha)
# print(comm.tree)
# print(comm.parents)
# print(comm.committer.name, comm.committer.email)
# print(comm.author.name, comm.author.email)
#
blob = Blob(repo, b'\xedH\xeb\xa2\x92w\xb0w\xf592\x81\xe5_\xe8\xf77\x87c\x8c')
print(blob.data_stream.read().decode('utf-8'))
print(blob.hexsha)


# commit=repo.active_branch.commit
# for item in commit.tree.traverse():
#     print(item,":",item.name)
#     print(item.type)
#     print(item.data_stream.read())
