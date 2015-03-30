# coding: utf-8

import os
import unittest
from pages.topic_page import CreatePage, CreateForm, TopicPage, BlogPage
from time import sleep
from selenium.webdriver import DesiredCapabilities, Remote
from selenium import webdriver

class CreateTopicTestCase(unittest.TestCase):
    BLOG = 'Флудилка'

    def setUp(self):
        # browser = os.environ.get('TTHA2BROWSER', 'CHROME')
        # self.driver = Remote(
        #     command_executor='http://127.0.0.1:4444/wd/hub',
        #     desired_capabilities=getattr(DesiredCapabilities, browser)
        # )
        self.driver = webdriver.Firefox()
        self.create_page = CreatePage(self.driver)
        self.create_page.open()

        # Authorization
        self.create_page.login()
        self.create_page.find_username()

        self.create_page.open()

    def tearDown(self):
        self.create_page.close()

    def test_create_and_delete_topic(self):
        title = u'Тестовый заголовок title'
        short_text = u'Короткий текст short text'
        main_text = u'Основной текст main text'

        create_form = CreateForm(self.driver)
        create_form.blog_select_open()
        create_form.blog_select_set_option(self.BLOG)
        create_form.set_title(title)
        create_form.set_short_text(short_text)
        create_form.set_main_text(main_text)
        create_form.submit()

        topic_page = TopicPage(self.driver)
        topic_title = unicode(topic_page.topic.get_title())
        topic_text = unicode(topic_page.topic.get_text())
        print "TOPIC TEXT"
        print(topic_text)
        self.assertEqual(title, topic_title)
        sleep(7)
        self.assertEqual(short_text, topic_text)
        sleep(4)
        topic_page.topic.open_blog()

        blog_page = BlogPage(self.driver)
        blog_page.topic.delete()
        topic_title = unicode(blog_page.topic.get_title())
        topic_text = unicode(blog_page.topic.get_text())
        self.assertNotEqual(title, topic_title)
        self.assertNotEqual(short_text, topic_text)

