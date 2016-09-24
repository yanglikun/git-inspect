__author__ = 'yanglikun'
from git import Repo
import os

repo = Repo(r'D:\worksapce\git\git-test')

for item in repo.iter_commits():
    # print(item.message)
    # print(item.hexsha)
    # print(item.parents)
    # print(item.committer.name, item.committer.email)
    # print(item.author.name, item.author.email)
    # print(tem.tree.abspath)
    tree=item.tree.trees[0]
    print(tree.name)
    break;
