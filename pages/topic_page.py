# coding: utf-8
from selenium.webdriver.support.wait import WebDriverWait

from base import Page
from component import Component


class CreatePage(Page):
    PATH = '/blog/topic/create/'

    @property
    def form(self):
        return CreateForm(self.driver)


class CreateForm(Component):
    BLOGSELECT = '//a[@class="chzn-single"]'
    OPTION = '//li[text()="{}"]'
    TITLE = '//input[@name="title"]'
    SHORT_TEXT = '//textarea[@name="text_short"]'
    MAIN_TEXT = '//textarea[@id="id_text"]'
    CREATE_BUTTON = '//button[contains(text(),"Создать")]'

    def blog_select_open(self):
        self.driver.find_element_by_xpath(self.BLOGSELECT).click()

    def blog_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION.format(option_text)).click()

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)

    def set_short_text(self, short_text):
        short_text_field = self.driver.find_element_by_xpath(self.SHORT_TEXT)
        short_text_field.send_keys(short_text)

    def set_main_text(self, main_text):
        self.driver.find_element_by_xpath(self.MAIN_TEXT).send_keys(main_text)

    def submit(self):
        self.driver.find_element_by_xpath(self.CREATE_BUTTON).click()


class Topic(Component):
    TITLE = '//*[@class="topic-title"]/a'
    TEXT = '//*[@class="topic-content text"]/p'
    BLOG = '//*[@class="topic-blog"]'
    DELETE_BUTTON = '//a[@class="actions-delete"]'
    DELETE_BUTTON_CONFIRM = '//input[@value="Удалить"]'

    def get_title(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TITLE).text
        )

    def get_text(self):
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(self.TEXT).text
        )

    def open_blog(self):
        self.driver.find_element_by_xpath(self.BLOG).click()

    def delete(self):
        self.driver.find_element_by_xpath(self.DELETE_BUTTON).click()
        self.driver.find_element_by_xpath(self.DELETE_BUTTON_CONFIRM).click()