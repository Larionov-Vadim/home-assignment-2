# coding: utf-8

import os
import unittest
from pages.topic_page import CreatePage, CreateForm
from time import sleep
from selenium.webdriver import DesiredCapabilities, Remote


class CreateTopicTestCase(unittest.TestCase):
    BLOG = 'Флудилка'

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser)
        )
        self.create_page = CreatePage(self.driver)
        self.create_page.open()
        self.create_page.login()
        # Необходимо дождаться авторизации
        # Временно sleep
        sleep(7)
        self.create_page.open()

    def tearDown(self):
        self.create_page.close()

    def test_create_topic(self):
        create_form = CreateForm(self.driver)
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(u'Обычный заголовок')
        # Вот тут Exception
        create_form.set_short_text(u'Листай дальше')
        create_form.set_main_text(u'Бла-бла-бла')
        create_form.submit()