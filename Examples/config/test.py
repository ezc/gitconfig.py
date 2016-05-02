#!/usr/bin/env python
from os.path import dirname, exists, join
from gitconfig import GitConfig

root=dirname(dirname(dirname(__file__)))
path=join(root,".git","config")
config=GitConfig(path)
print(config.sections)
