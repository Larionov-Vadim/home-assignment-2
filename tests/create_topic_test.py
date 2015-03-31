# coding: utf-8
import os
import unittest
from selenium.common.exceptions import NoSuchElementException
from pages.topic_page import CreatePage, TopicPage, BlogPage

__author__ = 'vadim'


class CreateTopicTestCase(unittest.TestCase):
    BLOG = 'Флудилка'

    def setUp(self):
        self.create_page = CreatePage()
        self.create_page.open_with_authorization()
        self.driver = self.create_page.get_driver()

    def tearDown(self):
        try:
            TopicPage(self.driver).topic.delete()
        except NoSuchElementException as ignore:
            pass
        self.create_page.close()

    def test_create_and_delete_topic(self):
        title = u'Тестовый заголовок title'
        short_text = u'Короткий текст short text'
        main_text = u'Основной текст main text'

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.form.submit()

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

        expected_tag = '<strong>'

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.form.select_short_text()
        self.create_page.form.bold_short_text_click()
        self.create_page.form.select_main_text()
        self.create_page.form.bold_main_text_click()
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        self.assertEqual(topic.get_title(), title)
        self.assertIn(expected_tag, topic.get_inner_html_content())

        topic.open_blog()
        blog = BlogPage(self.driver).blog
        self.assertEqual(blog.get_title(), title)
        self.assertIn(expected_tag, blog.get_inner_html_content())

    def test_italic_short_text(self):
        title = u'Title test check italic text'
        short_text = u'Italic short text'
        main_text = u'ignore'

        expected_tag = '<em>'

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.form.select_short_text()
        self.create_page.form.italic_short_text_click()
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        topic.open_blog()
        blog = BlogPage(self.driver).blog
        self.assertIn(expected_tag, blog.get_inner_html_content())

    def test_quote_short_text(self):
        title = u'Title, проверка цитирования'
        short_text = u'Цитируемый короткий текст, short text'
        main_text = u'ignore'

        expected_tag = '&gt;'

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.form.select_short_text()
        self.create_page.form.quote_short_text_click()
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        topic.open_blog()
        blog = BlogPage(self.driver).blog
        self.assertIn(expected_tag, blog.get_inner_html_content())

    def test_list_with_num_and_bold_main_text(self):
        title = u'Список с нумерацией, выделенный жирным текстом'
        short_text = u'ignore short text'
        main_text = u'TODO\n123'

        expected_main_text = '<strong>1. TODO<br>\n2. 123</strong>'

        self.create_page.form.list_with_num_main_text_click()
        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.form.select_main_text()
        self.create_page.form.bold_main_text_click()
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        self.assertEqual(topic.get_inner_html_text(), expected_main_text)

    def test_add_link_main_text(self):
        title = u'Title'
        short_text = u'ignore short text'
        main_text = u''

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.form.add_link_to_main_text(u'http://tech-mail.ru', u'Технопарк')
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        self.assertIn('href="http://tech-mail.ru"', topic.get_inner_html_content())
        self.assertEqual(u'Технопарк', topic.get_text())

    def test_insert_image(self):
        from_url = u'http://www.zadira.mk.ua/gallery/photos/11530_b.jpg'
        title = u'Загрузка изображения с внешнего ресурса'
        short_text = u''
        main_text = u'ignore'

        expected_tag = '<img'
        expected_src = 'src="' + from_url + '"'

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.form.insert_image_to_short_text(from_url)
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        topic.open_blog()
        blog = BlogPage(self.driver).blog
        self.assertIn(expected_tag, blog.get_inner_html_content())
        self.assertIn(expected_src, blog.get_inner_html_content())

    def test_upload_image(self):
        path_to_image = os.getcwdu() + u'/../image.png'
        title = u'Загрузка изображения с локального компьютера'

        expected_tag = '<img'

        self.create_page.create_simple_topic(self.BLOG, title, short_text='ignore', main_text=u'')
        self.create_page.form.upload_image_to_main_text(path_to_image)
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        self.assertIn(expected_tag, topic.get_inner_html_content())
        topic.delete()

    def test_add_poll_correct(self):
        title = u'Топик с опросом'
        short_text = u'В топике опрос'
        main_text = u'Опрос'

        question = u'Сколько Вы видите вариантов ответа?'
        expected_answers = [u'1', u'Два', u'3 жэ']

        self.create_page.create_simple_topic(self.BLOG, title, short_text, main_text)
        self.create_page.form.add_poll(question, *expected_answers)
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        actual_answers = topic.get_poll_answers()
        self.assertEqual(expected_answers, actual_answers)
