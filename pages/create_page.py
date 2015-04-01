# coding: utf-8
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from component import Component
from pages.actions import Actions
from pages.base import Page

__author__ = 'vadim'


class CreatePage(Page):
    PATH = '/blog/topic/create/'
    INFO_BLOCK = '//*[@id="block_blog_info"]'
    ERRORS_MSG = '//*[@class="system-message-error"]'

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

    def get_info(self):
        return Actions(self.driver).wait_and_get_text(By.XPATH, self.INFO_BLOCK)

    def has_errors(self):
        try:
            self.driver.find_element_by_xpath(self.ERRORS_MSG).is_displayed()
            return True
        except NoSuchElementException:
            return False


class CreateForm(Component):
    # <locators>
    BLOGSELECT = '//a[@class="chzn-single"]'
    OPTION = '//li[text()="{}"]'
    OPTION_BLOG_ID = '//*[@id="id_blog_chzn_o_{}"]'
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
    INSERT_IMG_SHORT_TEXT = '(//*[@title="Вставить изображение"])[1]'
    INSERT_IMG_MAIN_TEXT = '(//*[@title="Вставить изображение"])[2]'
    ADD_USER_SHORT_TEXT = '(//*[@title="Добавить пользователя"])[1]'
    ADD_USER_MAIN_TEXT = '(//*[@title="Добавить пользователя"])[2]'

    INPUT_FILEDATA_SHORT_TEXT = '(//*[@name="filedata"])[1]'
    INPUT_FILEDATA_MAIN_TEXT = '(//*[@name="filedata"])[2]'

    SEARCH_USER_POPUP = './/*[@id="search-user-login-popup"]'

    ADD_POLL_CHECKBOX = '//*[@class="input-checkbox add-poll"]'
    QUESTION_POLL = '//*[@id="id_question"]'
    ANSWEAR_POLL = '(//*[@id="id_form-{}-answer"])'
    ADD_OPTION_ANSWER = '//*[contains(text(),"Добавить вариант")]'
    DELETE_OPTION_ANSWER = '//*[@title="Удалить" and not(@style="display: none;")]'

    FORBID_COMMENT = '//*[@id="id_forbid_comment"]'
    # </locators>

    # <scripts>
    SHOW_UPLOAD_PHOTO_CONTAINER_SCRIPT = '$(".markdown-upload-photo-container").show()'
    # </scripts>

    def blog_select_open(self):
        self.driver.find_element_by_xpath(self.BLOGSELECT).click()

    def blog_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION.format(option_text)).click()

    def blog_select_by_id(self, option_id):
        self.driver.find_element_by_xpath(self.OPTION_BLOG_ID.format(option_id)).click()

    def set_title(self, title):
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)

    def set_short_text(self, short_text):
        short_text_field = self.driver.find_element_by_xpath(self.SHORT_TEXT)
        ActionChains(self.driver).click(short_text_field).send_keys(short_text).perform()

    def set_main_text(self, main_text):
        main_text_field = self.driver.find_element_by_xpath(self.MAIN_TEXT)
        ActionChains(self.driver).click(main_text_field).send_keys(main_text).perform()

    def submit(self):
        Actions(self.driver).click_to_element(By.XPATH, self.CREATE_BUTTON)

    # <Доступ по клику к элементам>
    def bold_short_text_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.BOLD_SHORT_TEXT)

    def bold_main_text_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.BOLD_MAIN_TEXT)

    def italic_short_text_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.ITALIC_SHORT_TEXT)

    def italic_main_text_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.ITALIC_MAIN_TEXT)

    def quote_short_text_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.QUOTE_SHORT_TEXT)

    def quote_main_text_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.QUOTE_MAIN_TEXT)

    def list_short_text_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.LIST_SHORT_TEXT)

    def list_main_text_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.LIST_MAIN_TEXT)

    def list_with_num_short_text_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.LIST_WITH_NUM_SHORT_TEXT)

    def list_with_num_main_text_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.LIST_WITH_NUM_MAIN_TEXT)

    def add_poll_checkbox_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.ADD_POLL_CHECKBOX)

    def add_additional_answer_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.ADD_OPTION_ANSWER)

    def delete_additional_answer_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.DELETE_OPTION_ANSWER)

    def forbid_comment_click(self):
        Actions(self.driver).click_to_element(By.XPATH, self.FORBID_COMMENT)

    # </Доступ по клику к элементам>

    # <Выделение текста>
    def select_main_text(self):
        Actions(self.driver).select_text(By.XPATH, self.MAIN_TEXT)

    def select_short_text(self):
        Actions(self.driver).select_text(By.XPATH, self.SHORT_TEXT)
    # </Выделение текста>

    def add_link_to_short_text(self, url, name):
        actions = Actions(self.driver)
        actions.click_to_element(By.XPATH, self.ADD_LINK_SHORT_TEXT)
        actions.wait_alert()
        actions.set_text_to_alert(url)
        actions.send_keys_and_perform(name)

    def add_link_to_main_text(self, url, name):
        actions = Actions(self.driver)
        actions.click_to_element(By.XPATH, self.ADD_LINK_MAIN_TEXT)
        actions.wait_alert()
        actions.set_text_to_alert(url)
        actions.send_keys_and_perform(name)

    def insert_image_to_short_text(self, from_url, name=''):
        actions = Actions(self.driver)
        actions.click_to_element(By.XPATH, self.INSERT_IMG_SHORT_TEXT)
        actions.wait_alert()
        actions.set_text_to_alert(from_url)
        actions.send_keys_and_perform(name)

    def insert_image_to_main_text(self, url, name=''):
        actions = Actions(self.driver)
        actions.click_to_element(By.XPATH, self.INSERT_IMG_MAIN_TEXT)
        actions.wait_alert()
        actions.set_text_to_alert(url)
        actions.send_keys_and_perform(name)

    def upload_image_to_main_text(self, path_to_file):
        actions = Actions(self.driver)
        actions.execute_script(self.SHOW_UPLOAD_PHOTO_CONTAINER_SCRIPT)
        actions.send_keys_to_elem_and_perform(By.XPATH, self.INPUT_FILEDATA_MAIN_TEXT, path_to_file)
        actions.wait_until_text_not_empty(By.XPATH, self.MAIN_TEXT)

    def add_poll(self, question, *answers):
        actions = Actions(self.driver)
        actions.click_to_element(By.XPATH, self.ADD_POLL_CHECKBOX)
        actions.send_keys_to_elem_and_perform(By.XPATH, self.QUESTION_POLL, question)

        count = len(answers)
        for index in range(count):
            answer_xpath = self.ANSWEAR_POLL.format(index)
            if not actions.element_is_exist(By.XPATH, answer_xpath):
                answer_xpath += '[2]'
                actions.click_and_wait(By.XPATH, self.ADD_OPTION_ANSWER, By.XPATH, answer_xpath)
            actions.send_keys_to_elem_and_perform(By.XPATH, answer_xpath, answers[index])

    def add_user_to_short_text(self, name):
        actions = Actions(self.driver)
        actions.click_and_wait(By.XPATH, self.ADD_USER_SHORT_TEXT, By.XPATH, self.SEARCH_USER_POPUP)
        self.driver.find_element_by_xpath(self.SEARCH_USER_POPUP).click()
        actions.send_keys_to_elem_and_perform(By.XPATH, self.SEARCH_USER_POPUP, name)
        choose_user = '//*[contains(text(), "' + name + '")]'
        self.driver.find_element_by_xpath(choose_user).click()

    def add_user_to_main_text(self, name):
        actions = Actions(self.driver)
        actions.click_and_wait(By.XPATH, self.ADD_USER_MAIN_TEXT, By.XPATH, self.SEARCH_USER_POPUP)
        self.driver.find_element_by_xpath(self.SEARCH_USER_POPUP).click()
        actions.send_keys_to_elem_and_perform(By.XPATH, self.SEARCH_USER_POPUP, name)
        choose_user = '//*[contains(text(), "' + name + '")]'
        self.driver.find_element_by_xpath(choose_user).click()
