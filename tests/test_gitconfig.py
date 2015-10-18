#!/usr/bin/env python
from unittest import main, TestCase
from assert_is import is_
from gitconfig import config, gitconfig


class test(TestCase):
    def test(self):
        is_(gitconfig,config)

if __name__ == "__main__":
    main()