__author__ = 'yanglikun'
from git import Repo
import os
repo = Repo(r'D:\worksapce\git\git-test')
for (path, stage), entry in repo.index.entries.items():
    print(entry.path,entry.hexsha)

