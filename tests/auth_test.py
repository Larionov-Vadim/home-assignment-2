# coding: utf-8
import unittest
import config
from pages.base import Page

__author__ = 'vadim'


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.page = Page()
        self.page.open()

    def tearDown(self):
        self.page.close()

    def test_authentication(self):
        self.assertEqual(self.page.login(), config.USERNAME)