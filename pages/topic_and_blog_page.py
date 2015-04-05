# coding: utf-8
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.actions import Actions
from pages.base import Page
from pages.component import Component

__author__ = 'vadim'


class TopicPage(Page):
    @property
    def topic(self):
        return Topic(self.driver)


class Topic(Component):
    TITLE = '//*[@class="topic-title"]/a'
    TEXT = '//*[@class="topic-content text"]'
    BLOG = '//*[@class="topic-blog"]'
    DELETE_BUTTON = '//a[@class="actions-delete"]'
    DELETE_BUTTON_CONFIRM = '//input[@value="Удалить"]'
    # POLL_ANSWER = '//*[@class="poll-vote"]/li'
    ADD_COMMENT = '//*[contains(@class,"comment-add-link")]'

    def get_title(self):
        return Actions(self.driver).wait_and_get_text(By.XPATH, self.TITLE)

    def get_text(self):
        return Actions(self.driver).wait_and_get_text(By.XPATH, self.TEXT)

    def open_blog(self):
        Actions(self.driver).click_to_element(By.XPATH, self.BLOG)

    def delete(self):
        actions = Actions(self.driver)
        actions.click_to_element(By.XPATH, self.DELETE_BUTTON)
        actions.click_to_element(By.XPATH, self.DELETE_BUTTON_CONFIRM)

    def safe_delete(self):
        try:
            self.delete()
        except NoSuchElementException as ignore:
            pass    # Топик не существует

    def get_inner_html_text(self):
        return Actions(self.driver).wait_and_get_attribute(By.XPATH, self.TEXT, 'innerHTML')

    # def get_poll_answers(self):
    #     actions = Actions(self.driver)
    #     elements = actions.get_list_elements(By.XPATH, self.POLL_ANSWER)
    #     return actions.get_list_text_from_list_elements(*elements)

    def has_add_comment_btn(self):
        return Actions(self.driver).element_is_exist(By.XPATH, self.ADD_COMMENT)


class BlogPage(Page):
    @property
    def blog(self):
        return Topic(self.driver)
