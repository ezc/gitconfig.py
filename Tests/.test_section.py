#!/usr/bin/env python
from unittest import main, skip
from assert_is import eq_, in_, not_in, ok_
import base

class test(base.cls):
    #@skip("")
    def test_contains(self):
        in_("key",self.config.section)
        not_in("key88",self.config.section)

    #@skip("")
    def test_getitem(self):
        for s in self.config.__sections__:
            section=self.config[s]
            for key in section.__keys__:
                ok_(section[key])
                ok_(getattr(section,key))

    #@skip("")
    def test_set(self):
        self.config.section.key = "value"
        eq_(self.config.section.key, "value")

    #@skip("")
    def test_unset(self):
        self.config.section.key = "value"
        self.config.unset("section", "key")
        eq_(self.config.section.key, None)
        self.config.section.key = "value"
        self.config.section.key=None
        eq_(self.config.section.key, None)

if __name__ == "__main__":
    main()