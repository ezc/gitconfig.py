#!/usr/bin/env python
import os
from gitconfig import GitConfig

root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
path = os.path.join(root, ".git", "config")
config = GitConfig(path)
print(config.sections)
