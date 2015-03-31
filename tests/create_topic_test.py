# coding: utf-8
import os
import unittest
from pages.topic_page import CreatePage, CreateForm, TopicPage, BlogPage
from time import sleep
from selenium.webdriver import DesiredCapabilities, Remote
from selenium import webdriver
from selenium.webdriver import ActionChains

__author__ = 'vadim'


class CreateTopicTestCase(unittest.TestCase):
    BLOG = 'Флудилка'

    def setUp(self):
        self.create_page = CreatePage()
        self.create_page.open_with_authorization()
        self.driver = self.create_page.get_driver()

    def tearDown(self):
        self.create_page.close()

    def test_create_and_delete_topic(self):
        title = u'Тестовый заголовок title'
        short_text = u'Короткий текст short text'
        main_text = u'Основной текст main text'

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.submit_created_topic()

        topic = TopicPage(self.driver).topic
        self.assertEqual(topic.get_title(), title)
        self.assertEqual(topic.get_text(), main_text)

        topic.open_blog()
        blog = BlogPage(self.driver).blog
        self.assertEqual(blog.get_title(), title)
        self.assertEqual(blog.get_text(), short_text)
        topic.delete()

        self.assertNotEqual(blog.get_title(), title)
        self.assertNotEqual(blog.get_text(), short_text)

    def test_bold_text(self):
        title = u'Title test check bold text'
        short_text = u'Bold short text'
        main_text = u'Bold main text'

        expected_short_text = '<strong>' + short_text + '</strong>'
        expected_main_text = '<strong>' + main_text + '</strong>'

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.select_bold_short_text()
        self.create_page.select_bold_main_text()
        self.create_page.submit_created_topic()

        topic = TopicPage(self.driver).topic
        self.assertEqual(topic.get_title(), title)
        self.assertEqual(topic.get_inner_html_text(), expected_main_text)

        topic.open_blog()
        blog = BlogPage(self.driver).blog
        self.assertEqual(blog.get_title(), title)
        self.assertEqual(blog.get_inner_html_text(), expected_short_text)
        topic.delete()

    def test_italic_text(self):
        title = u'Title test check italic text'
        short_text = u'Italic short text'
        main_text = u'Italic main text'

        expected_short_text = '<em>' + short_text + '</em>'
        expected_main_text = '<em>' + main_text + '</em>'

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.select_italic_short_text()
        self.create_page.select_italic_main_text()
        self.create_page.submit_created_topic()

        topic = TopicPage(self.driver).topic
        self.assertEqual(topic.get_title(), title)
        self.assertEqual(topic.get_inner_html_text(), expected_main_text)

        topic.open_blog()
        blog = BlogPage(self.driver).blog
        self.assertEqual(blog.get_title(), title)
        self.assertEqual(blog.get_inner_html_text(), expected_short_text)
        topic.delete()

    def test_quote(self):
        title = u'Title, проверка цитирования'
        short_text = u'Цитируемый короткий текст, short text'
        main_text = u'Цитируемый основной текст, main text'

        expected_short_text = '&gt; ' + short_text
        expected_main_text = '&gt; ' + main_text

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.select_quote_short_text()
        self.create_page.select_quote_main_text()
        self.create_page.submit_created_topic()

        topic = TopicPage(self.driver).topic
        self.assertEqual(topic.get_title(), title)
        self.assertEqual(topic.get_inner_html_text(), expected_main_text)

        topic.open_blog()
        blog = BlogPage(self.driver).blog
        self.assertEqual(blog.get_title(), title)
        self.assertEqual(blog.get_inner_html_text(), expected_short_text)
        topic.delete()

    def test_list_with_num_and_bold_main_text(self):
        title = u'Список с нумерацией, выделенный жирным текстом'
        short_text = u'ignore short text'
        main_text = u'TODO\n123'

        expected_main_text = '<strong>1. TODO<br>\n2. 123</strong>'

        self.create_page.form.list_with_num_main_text_click()
        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.select_bold_main_text()
        self.create_page.submit_created_topic()

        topic = TopicPage(self.driver).topic
        self.assertEqual(topic.get_inner_html_text(), expected_main_text)
        topic.delete()

    def test_add_link(self):
        title = u'Title'
        short_text = u'ignore short text'
        main_text = u''

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.form.add_link_to_main_text(u'http://tech-mail.ru', u'Технопарк')
        self.create_page.submit_created_topic()

        topic = TopicPage(self.driver).topic
        self.assertIn('href="http://tech-mail.ru"', topic.get_inner_html_content())
        self.assertEqual(u'Технопарк', topic.get_text())
        topic.delete()