# coding: utf-8
import os
import unittest
from pages.create_page import CreatePage
from pages.topic_and_blog_page import TopicPage, BlogPage

__author__ = 'vadim'


class CreateTopicTestCase(unittest.TestCase):
    BLOG = 'Флудилка'

    def setUp(self):
        self.create_page = CreatePage()
        self.create_page.open_with_authorization()
        self.driver = self.create_page.get_driver()

    def tearDown(self):
        TopicPage(self.driver).topic.safe_delete()
        self.create_page.close()

    def test_create_simple_topic(self):
        title = u'Тестовый заголовок'
        main_text = u'Основной текст'

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        self.assertEqual(topic.get_title(), title)
        self.assertEqual(topic.get_text(), main_text)

        topic.open_blog()
        blog = BlogPage(self.driver).blog
        self.assertEqual(blog.get_title(), title)
        self.assertEqual(blog.get_text(), main_text)
        topic.delete()

        self.assertNotEqual(blog.get_title(), title)
        self.assertNotEqual(blog.get_text(), main_text)

    def test_cut_tag(self):
        title = u'Тестирование тега <cut>'
        short_text = u'Текст в блоге'
        main_text = u'Текст в топике'

        text = short_text + u'<cut>' + main_text + u'</cut>'
        self.create_page.create_simple_topic(self.BLOG, title, text)
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        self.assertEqual(topic.get_title(), title)
        self.assertEqual(topic.get_text(), short_text + u' ' + main_text)

        topic.open_blog()
        blog = BlogPage(self.driver).blog
        self.assertIn(short_text, blog.get_text())
        self.assertNotIn(main_text, blog.get_text())

    def test_h4_text(self):
        title = u'Проверка текста H4'
        main_text = u'Заголовок четвертого уровня'

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.select_main_text()
        self.create_page.form.h4_text_click()
        self.create_page.form.submit()

        expected_str = '<h4>' + main_text + '</h4>'

        topic = TopicPage(self.driver).topic
        self.assertIn(expected_str, topic.get_inner_html_text())

        topic.open_blog()
        blog = BlogPage(self.driver).blog
        self.assertIn(expected_str, blog.get_inner_html_text())

    def test_h5_text(self):
        title = u'Проверка текста H5'
        main_text = u'Заголовок пятого уровня'

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.select_main_text()
        self.create_page.form.h5_text_click()
        self.create_page.form.submit()

        expected_str = '<h5>' + main_text + '</h5>'

        topic = TopicPage(self.driver).topic
        self.assertIn(expected_str, topic.get_inner_html_text())

    def test_h6_text(self):
        title = u'Проверка текста H6'
        main_text = u'Заголовок шестого уровня'

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.select_main_text()
        self.create_page.form.h6_text_click()
        self.create_page.form.submit()

        expected_str = '<h6>' + main_text + '</h6>'

        topic = TopicPage(self.driver).topic
        self.assertIn(expected_str, topic.get_inner_html_text())

    def test_bold_text(self):
        title = u'Проверка жирного текста'
        main_text = u'Жирный текст'

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.select_main_text()
        self.create_page.form.bold_text_click()
        self.create_page.form.submit()

        expected_str = '<strong>' + main_text + '</strong>'

        topic = TopicPage(self.driver).topic
        self.assertIn(expected_str, topic.get_inner_html_text())

    def test_italic_text(self):
        title = u'Проверка курсива'
        main_text = u'Курсив'

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.select_main_text()
        self.create_page.form.italic_text_click()
        self.create_page.form.submit()

        expected_str = '<em>' + main_text + '</em>'

        topic = TopicPage(self.driver).topic
        self.assertIn(expected_str, topic.get_inner_html_text())

    def test_strikethrough_text(self):
        title = u'Проверка перечеркнутого текста'
        main_text = u'Этот текст будет зачеркнут'

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.select_main_text()
        self.create_page.form.strikethrough_text_click()
        self.create_page.form.submit()

        expected_str = '<s>' + main_text + '</s>'

        topic = TopicPage(self.driver).topic
        self.assertIn(expected_str, topic.get_inner_html_text())

    def test_quote_text(self):
        title = u'Проверка цитирования'
        main_text = u'Цитата'

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.select_main_text()
        self.create_page.form.quote_click()
        self.create_page.form.submit()

        expected_str = '<blockquote>' + main_text + '</blockquote>'

        topic = TopicPage(self.driver).topic
        self.assertIn(expected_str, topic.get_inner_html_text())

    def test_code_text(self):
        title = u'Проверка тега <code>'
        main_text = u'printf("test_code");'

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.select_main_text()
        self.create_page.form.code_click()
        self.create_page.form.submit()

        expected_str = '<code>' + main_text + '</code>'

        topic = TopicPage(self.driver).topic
        self.assertIn(expected_str, topic.get_inner_html_text())

    def test_marked_list(self):
        title = u'Проверка маркерованного списка'
        first_node = u'Первая строка маркерованного списка'
        second_node = u'Вторая строка маркерованного списка'
        main_text = first_node + u'\n' + second_node

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.select_main_text()
        self.create_page.form.list_click()
        self.create_page.form.submit()

        expected_tag = '<ul>'
        expected_first_node = '<li>' + first_node + '</li>'
        expected_second_node = '<li>' + second_node + '</li>'

        topic = TopicPage(self.driver).topic
        actual_inner_html = topic.get_inner_html_text()
        self.assertIn(expected_tag, actual_inner_html)
        self.assertIn(expected_first_node, actual_inner_html)
        self.assertIn(expected_second_node, actual_inner_html)

    def test_numbered_list(self):
        title = u'Проверка нумерованного списка'
        first_node = u'Первая строка нумерованного списка'
        second_node = u'Вторая строка нумерованного списка'
        main_text = first_node + u'\n' + second_node

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.select_main_text()
        self.create_page.form.numbered_list_click()
        self.create_page.form.submit()

        expected_tag = '<ol>'
        expected_first_node = '<li>' + first_node + '</li>'
        expected_second_node = '<li>' + second_node + '</li>'

        TopicPage(self.driver).topic.open_blog()
        blog = BlogPage(self.driver).blog
        actual_inner_html = blog.get_inner_html_text()
        self.assertIn(expected_tag, actual_inner_html)
        self.assertIn(expected_first_node, actual_inner_html)
        self.assertIn(expected_second_node, actual_inner_html)

    def test_add_link(self):
        title = u'Вставка ссылки'
        main_text = u''

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.add_link_to_main_text(u'http://tech-mail.ru', u'Технопарк')
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        self.assertIn('href="http://tech-mail.ru"', topic.get_inner_html_text())
        self.assertEqual(u'Технопарк', topic.get_text())

    def test_add_user(self):
        title = u'Добавление пользователя'
        main_text = u''
        user = u'Баяндин'

        expected_attr = 'href='

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.add_user(user)
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        inner_html = topic.get_inner_html_text()
        self.assertIn(expected_attr, inner_html)
        self.assertIn(user, inner_html)

    def test_add_poll(self):
        title = u'Топик с опросом'
        main_text = u'Опрос'

        question = u'Сколько Вы видите вариантов ответа?'
        expected_answers = [u'1', u'Два', u'3 жэ']

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.add_poll(question, *expected_answers)
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        actual_answers = topic.get_poll_answers()
        self.assertEqual(expected_answers, actual_answers)

    def test_upload_image(self):
        path_to_image = unicode(os.path.dirname(__file__)) + u'/../images/image.png'
        title = u'Загрузка изображения с локального компьютера'
        align = u'left'
        description = u'Кот'

        expected_tag = '<img'
        expected_align = 'align="' + align + '"'
        expected_description = 'title="' + description + '"'

        self.create_page.create_simple_topic(self.BLOG, title, main_text=u'')
        self.create_page.form.upload_image(path_to_image, align, description)
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        inner_html = topic.get_inner_html_text()
        self.assertIn(expected_tag, inner_html)
        self.assertIn(expected_align, inner_html)
        self.assertIn(expected_description, inner_html)

    def test_insert_image(self):
        from_url = u'http://www.zadira.mk.ua/gallery/photos/11530_b.jpg'
        title = u'Загрузка изображения с внешнего ресурса'
        align = u'center'
        desctiption = u'Медведь'

        expected_tag = '<img'
        expected_align = 'align="' + align + '"'
        expected_description = 'title="' + desctiption + '"'

        self.create_page.create_simple_topic(self.BLOG, title, u'')
        self.create_page.form.insert_image(from_url, align, desctiption)
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        topic.open_blog()
        blog = BlogPage(self.driver).blog
        inner_html = blog.get_inner_html_text()
        self.assertIn(expected_tag, inner_html)
        self.assertIn(expected_align, inner_html)
        self.assertIn(expected_description, inner_html)

    def test_insert_image_as_link(self):
        from_url = u'http://www.zadira.mk.ua/gallery/photos/11530_b.jpg'
        title = u'Загрузка изображения с внешнего ресурса в качестве ссылки'
        align = u'right'
        desctiption = u'Медведь'

        expected_tag = '<img'
        expected_align = 'align="' + align + '"'
        expected_description = 'title="' + desctiption + '"'
        expected_src = from_url

        self.create_page.create_simple_topic(self.BLOG, title, u'')
        self.create_page.form.insert_image(from_url, align, desctiption, as_link=True)
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        topic.open_blog()
        blog = BlogPage(self.driver).blog
        inner_html = blog.get_inner_html_text()
        self.assertIn(expected_tag, inner_html)
        self.assertIn(expected_src, inner_html)
        self.assertIn(expected_align, inner_html)
        self.assertIn(expected_description, inner_html)

    def test_without_title(self):
        main_text = u'Топик без заголовка'

        self.create_page.form.set_main_text(main_text)
        self.create_page.form.submit()
        self.assertTrue(self.create_page.has_errors())

    def test_without_main_text(self):
        title = u'Tопик без основного текста'

        self.create_page.form.blog_select_open()
        self.create_page.form.blog_select_set_option(self.BLOG)
        self.create_page.form.set_title(title)
        self.create_page.form.submit()
        self.assertTrue(self.create_page.has_errors())

    def test_empty_fields(self):
        self.create_page.form.submit()
        self.assertTrue(self.create_page.has_errors())

    def test_add_poll_with_empty_fields(self):
        title = u'Топик с добавлением опроса, но без вопроса и вариантов'
        main_text = u'main text'

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.add_poll('', [])
        self.create_page.form.submit()
        self.assertTrue(self.create_page.has_errors())

    def test_create_topic_with_forbid_comments(self):
        title = u'Топик с закрытыми комментариями'
        main_text = u'main text'

        self.create_page.create_simple_topic(self.BLOG, title, main_text)
        self.create_page.form.forbid_comment_click()
        self.create_page.form.submit()

        topic = TopicPage(self.driver).topic
        self.assertFalse(topic.has_add_comment_btn())
