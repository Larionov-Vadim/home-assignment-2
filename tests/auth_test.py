# coding: utf-8

import os
import unittest
import config
from selenium.webdriver import DesiredCapabilities, Remote
from pages.base import Page


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser)
        )
        self.page = Page(self.driver)
        self.page.open()

    def tearDown(self):
        self.page.close()

    def test_authentication(self):
        self.page.login()
        self.assertEqual(self.page.find_username(), config.USERNAME)