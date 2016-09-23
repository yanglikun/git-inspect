__author__ = 'yanglikun'
from git import Repo
import os
repo = Repo(r'D:\worksapce\git\git-test')
print(repo.is_dirty())
print(repo.untracked_files)
print(repo.working_tree_dir)

#分支
branches=repo.heads
print(branches)
print(repo.head.name)
print('a' in branches,'master' in branches, 'HEAD' in branches)

#引用指向commit
refs=repo.refs
print(refs)

current=repo.active_branch
commit=current.commit
print(commit,commit.message)
print(commit.tree)

print("===tree====")
for item in commit.tree.traverse():
    print(item)

print("=====index===")
for item in repo.index.entries:
    print(item)