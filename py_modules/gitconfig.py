#!/usr/bin/env python
import git
from conf import *
from fullpath import fullpath
from public import public

GitConfigParser=git.config.GitConfigParser

@public
class Gitconfig(Conf):
    read_only = False

    def __init__(self,path,read_only=False):
        self.read_only = read_only
        path = fullpath(path)
        parser = GitConfigParser(path,read_only=self.read_only)
        Conf.__init__(self,path=path,parser=parser)

    def write(self):
        self.parser.write()

gitconfig = Gitconfig("~/.gitconfig",True)
public(gitconfig)
