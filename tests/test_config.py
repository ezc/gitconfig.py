#!/usr/bin/env python
from unittest import main, skip
from assert_is import eq_, in_, not_in, is_, is_list
from file import fullpath
from configcls import sectioncls
import base

class test(base.cls):
    #@skip("")
    def test_fullpath(self):
        eq_(fullpath(self.f), self.config.fullpath)

    #@skip("")
    def test_contains(self):
        in_("section",self.config)
        not_in("section88",self.config)

    #@skip("")
    def test_sections(self):
        is_list(self.config.__sections__)
        for s in self.config.__sections__:
            is_(self.config[s],sectioncls)

if __name__ == "__main__":
    main()