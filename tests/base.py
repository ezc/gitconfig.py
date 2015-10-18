#!/usr/bin/env python
from unittest import TestCase
from file import exists, unlink
from gitconfig import config

class cls(TestCase):
    def setUp(self):
        self.config.section.key="value"
        self.config.section2.key2="value2"

    @classmethod
    def setUpClass(cls):
        cls.f = ".test"
        cls.config = None
        if exists(cls.f):
            unlink(cls.f)
        cls.config = config(cls.f)


    @classmethod
    def tearDownClass(cls):
        del cls.config