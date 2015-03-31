# coding: utf-8
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.selenium import selenium
from selenium import webdriver

from base import Page
from component import Component

__author__ = 'vadim'


class CreatePage(Page):
    PATH = '/blog/topic/create/'

    @property
    def form(self):
        return CreateForm(self.driver)

    def open_with_authorization(self):
        self.open()
        self.login()
        self.open()

    def create_simple_topic(self, blog, title, short_text, main_text):
        create_form = self.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(blog)
        create_form.set_title(title)
        create_form.set_short_text(short_text)
        create_form.set_main_text(main_text)

    def submit_created_topic(self):
        self.form.submit()

    def select_bold_short_text(self):
        self.form.select_short_text()
        self.form.bold_short_text_click()

    def select_bold_main_text(self):
        self.form.select_main_text()
        self.form.bold_main_text_click()

    def select_italic_short_text(self):
        self.form.select_short_text()
        self.form.italic_short_text_click()

    def select_italic_main_text(self):
        self.form.select_main_text()
        self.form.italic_main_text_click()

    def select_quote_short_text(self):
        self.form.select_short_text()
        self.form.quote_short_text_click()

    def select_quote_main_text(self):
        self.form.select_main_text()
        self.form.quote_main_text_click()

    def select_list_short_text(self):
        self.form.select_short_text()
        self.form.list_short_text_click()

    def select_list_main_text(self):
        self.form.select_main_text()
        self.form.list_main_text_click()

    def select_list_with_num_short_text(self):
        self.form.select_short_text()
        self.form.list_with_num_short_text_click()

    def select_list_with_num_main_text(self):
        self.form.select_main_text()
        self.form.list_with_num_main_text_click()


class CreateForm(Component):
    BLOGSELECT = '//a[@class="chzn-single"]'
    OPTION = '//li[text()="{}"]'
    TITLE = '//input[@name="title"]'
    SHORT_TEXT = '(//*[@class="CodeMirror-scroll"])[1]'     # xpath short_text
    MAIN_TEXT = '(//*[@class="CodeMirror-scroll"])[2]'      # xpath main_text
    CREATE_BUTTON = '//button[contains(text(),"Создать")]'

    BOLD_SHORT_TEXT = '(//*[@title="Жирный"])[1]'
    BOLD_MAIN_TEXT = '(//*[@title="Жирный"])[2]'
    ITALIC_SHORT_TEXT = '(//*[@title="Курсив"])[1]'
    ITALIC_MAIN_TEXT = '(//*[@title="Курсив"])[2]'
    QUOTE_SHORT_TEXT = '(//*[@title="Цитировать"])[1]'
    QUOTE_MAIN_TEXT = '(//*[@title="Цитировать"])[2]'
    LIST_SHORT_TEXT = '(//*[@title="Список"])[1]'
    LIST_MAIN_TEXT = '(//*[@title="Список"])[2]'
    LIST_WITH_NUM_SHORT_TEXT = '(//*[@title="Список с нумерацией"])[1]'
    LIST_WITH_NUM_MAIN_TEXT = '(//*[@title="Список с нумерацией"])[2]'
    ADD_LINK_SHORT_TEXT = '(//*[@title="Вставить ссылку"])[1]'
    ADD_LINK_MAIN_TEXT = '(//*[@title="Вставить ссылку"])[2]'

    def blog_select_open(self):
        self.driver.find_element_by_xpath(self.BLOGSELECT).click()

    def blog_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION.format(option_text)).click()

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)

    def set_short_text(self, short_text):
        short_text_field = self.driver.find_element_by_xpath(self.SHORT_TEXT)
        ActionChains(self.driver).click(short_text_field).send_keys(short_text).perform()

    def set_main_text(self, main_text):
        main_text_field = self.driver.find_element_by_xpath(self.MAIN_TEXT)
        ActionChains(self.driver).click(main_text_field).send_keys(main_text).perform()

    def submit(self):
        self.driver.find_element_by_xpath(self.CREATE_BUTTON).click()

    def bold_short_text_click(self):
        self.driver.find_element_by_xpath(self.BOLD_SHORT_TEXT).click()

    def bold_main_text_click(self):
        self.driver.find_element_by_xpath(self.BOLD_MAIN_TEXT).click()

    def italic_short_text_click(self):
        self.driver.find_element_by_xpath(self.ITALIC_SHORT_TEXT).click()

    def italic_main_text_click(self):
        self.driver.find_element_by_xpath(self.ITALIC_MAIN_TEXT).click()

    def quote_short_text_click(self):
        self.driver.find_element_by_xpath(self.QUOTE_SHORT_TEXT).click()

    def quote_main_text_click(self):
        self.driver.find_element_by_xpath(self.QUOTE_MAIN_TEXT).click()

    def list_short_text_click(self):
        self.driver.find_element_by_xpath(self.LIST_SHORT_TEXT).click()

    def list_main_text_click(self):
        self.driver.find_element_by_xpath(self.LIST_MAIN_TEXT).click()

    def list_with_num_short_text_click(self):
        self.driver.find_element_by_xpath(self.LIST_WITH_NUM_SHORT_TEXT).click()

    def list_with_num_main_text_click(self):
        self.driver.find_element_by_xpath(self.LIST_WITH_NUM_MAIN_TEXT).click()

    def select_main_text(self):
        ActionChains(self.driver).\
            click(self.driver.find_element_by_xpath(self.MAIN_TEXT)).\
            key_down(Keys.CONTROL).\
            key_down("a").\
            key_up(Keys.CONTROL).\
            perform()

    def select_short_text(self):
        ActionChains(self.driver).\
            click(self.driver.find_element_by_xpath(self.SHORT_TEXT)).\
            key_down(Keys.CONTROL).\
            key_down("a").\
            key_up(Keys.CONTROL).\
            perform()

    def add_link_to_short_text(self, url, name):
        self.driver.find_element_by_xpath(self.ADD_LINK_SHORT_TEXT).click()
        WebDriverWait(self.driver, timeout=30, poll_frequency=0.1).\
            until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(url)
        alert.accept()
        ActionChains(self.driver).send_keys(name).perform()

    def add_link_to_main_text(self, url, name):
        self.driver.find_element_by_xpath(self.ADD_LINK_MAIN_TEXT).click()
        WebDriverWait(self.driver, timeout=30, poll_frequency=0.1).\
            until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.send_keys(url)
        alert.accept()
        ActionChains(self.driver).send_keys(name).perform()


class TopicPage(Page):
    @property
    def topic(self):
        return Topic(self.driver)


class Topic(Component):
    TITLE = '//*[@class="topic-title"]/a'
    TEXT = '//*[@class="topic-content text"]/p'
    LIST = '//*[@class="topic-content text"]/ul'
    BLOG = '//*[@class="topic-blog"]'
    DELETE_BUTTON = '//a[@class="actions-delete"]'
    DELETE_BUTTON_CONFIRM = '//input[@value="Удалить"]'
    CONTENT = '//*[@class="topic-content text"]'

    def get_title(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE).text
        )

    def get_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT).text
        )

    def get_list(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LIST).text
        )

    def open_blog(self):
        self.driver.find_element_by_xpath(self.BLOG).click()

    def delete(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_CONFIRM).click()

    def get_inner_html_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT).get_attribute('innerHTML')
        )

    def get_inner_html_list(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.LIST).get_attribute('innerHTML')
        )

    def get_inner_html_content(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.CONTENT).get_attribute('innerHTML')
        )


class BlogPage(Page):
    @property
    def blog(self):
        return Topic(self.driver)
