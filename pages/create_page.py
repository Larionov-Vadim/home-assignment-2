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

    def create_simple_topic(self, blog, title, main_text):
        create_form = self.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(blog)
        create_form.set_title(title)
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
    OPTION_BLOG_ID = '//*[@id="id_blog_chzn_o_{}"]'     # TODO ?
    TITLE = '//input[@name="title"]'
    MAIN_TEXT = '//*[@id="id_text"]'
    CREATE_BUTTON = '//button[contains(text(),"Создать")]'

    #H4_BUTTON = '//a[@title="H4"]'
    H4_BUTTON = './/*[@id="markItUpId_text"]/div/div[1]/ul/li[1]/a'
    #H5_BUTTON = '//*[@title="H5"]'
    H5_BUTTON = './/*[@id="markItUpId_text"]/div/div[1]/ul/li[2]/a'
    #H6_BUTTON = '//*[@title="H6"]'
    H6_BUTTON = './/*[@id="markItUpId_text"]/div/div[1]/ul/li[3]/a'

    #BOLD_TEXT = '//*[contains(text(),"жирный")]'
    BOLD_TEXT = './/*[@id="markItUpId_text"]/div/div[1]/ul/li[5]/a'
    #ITALIC_TEXT = '//*[contains(text(),"курсив")]'
    ITALIC_TEXT = './/*[@id="markItUpId_text"]/div/div[1]/ul/li[6]/a'
    #STRIKETHROUGH_TEXT = '//*[contains(text(),"зачеркнутый")]'
    STRIKETHROUGH_TEXT = './/*[@id="markItUpId_text"]/div/div[1]/ul/li[7]/a'
    #UNDERLINE_TEXT = '//*[contains(text(),"подчеркнутый")]'
    UNDERLINE_TEXT = './/*[@id="markItUpId_text"]/div/div[1]/ul/li[8]/a'

    #QUOTE = '//*[contains(text(),"цитировать")]'
    QUOTE = './/*[@id="markItUpId_text"]/div/div[1]/ul/li[9]/a'
    #CODE = '//*[@title="код"]'
    CODE = './/*[@id="markItUpId_text"]/div/div[1]/ul/li[10]/a'

    LIST = './/*[@id="markItUpId_text"]/div/div[1]/ul/li[12]/a'
    NUMBERED_LIST = './/*[@id="markItUpId_text"]/div/div[1]/ul/li[13]/a'

    # LIST_SHORT_TEXT = '(//*[@title="Список"])[1]'
    # LIST_MAIN_TEXT = '(//*[@title="Список"])[2]'
    # LIST_WITH_NUM_SHORT_TEXT = '(//*[@title="Список с нумерацией"])[1]'
    # LIST_WITH_NUM_MAIN_TEXT = '(//*[@title="Список с нумерацией"])[2]'
    # ADD_LINK_SHORT_TEXT = '(//*[@title="Вставить ссылку"])[1]'
    # ADD_LINK_MAIN_TEXT = '(//*[@title="Вставить ссылку"])[2]'
    # INSERT_IMG_SHORT_TEXT = '(//*[@title="Вставить изображение"])[1]'
    # INSERT_IMG_MAIN_TEXT = '(//*[@title="Вставить изображение"])[2]'
    # ADD_USER_SHORT_TEXT = '(//*[@title="Добавить пользователя"])[1]'
    # ADD_USER_MAIN_TEXT = '(//*[@title="Добавить пользователя"])[2]'
    #
    # INPUT_FILEDATA_SHORT_TEXT = '(//*[@name="filedata"])[1]'
    # INPUT_FILEDATA_MAIN_TEXT = '(//*[@name="filedata"])[2]'
    #
    # SEARCH_USER_POPUP = './/*[@id="search-user-login-popup"]'
    #
    # ADD_POLL_CHECKBOX = '//*[@class="input-checkbox add-poll"]'
    # QUESTION_POLL = '//*[@id="id_question"]'
    # ANSWEAR_POLL = '(//*[@id="id_form-{}-answer"])'
    # ADD_OPTION_ANSWER = '//*[contains(text(),"Добавить вариант")]'
    # DELETE_OPTION_ANSWER = '//*[@title="Удалить" and not(@style="display: none;")]'
    #
    # FORBID_COMMENT = '//*[@id="id_forbid_comment"]'
    # # </locators>
    #
    # # <scripts>
    # SHOW_UPLOAD_PHOTO_CONTAINER_SCRIPT = '$(".markdown-upload-photo-container").show()'
    # # </scripts>
    #
    def blog_select_open(self):
        self.driver.find_element_by_xpath(self.BLOGSELECT).click()

    def blog_select_set_option(self, option_text):
        self.driver.find_element_by_xpath(self.OPTION.format(option_text)).click()
    #
    # def blog_select_by_id(self, option_id):
    #     self.driver.find_element_by_xpath(self.OPTION_BLOG_ID.format(option_id)).click()
    #
    def set_title(self, title):
        self.driver.find_element_by_xpath(self.TITLE).send_keys(title)

    def set_main_text(self, main_text):
        main_text_field = self.driver.find_element_by_xpath(self.MAIN_TEXT)
        ActionChains(self.driver).click(main_text_field).send_keys(main_text).perform()

    def submit(self):
        Actions(self.driver).click_to_element(By.XPATH, self.CREATE_BUTTON)

    # <Доступ по клику к элементам>
    def h4_text_click(self):
        Actions(self.driver).wait_and_click(By.XPATH, self.H4_BUTTON)

    def h5_text_click(self):
        Actions(self.driver).wait_and_click(By.XPATH, self.H5_BUTTON)

    def h6_text_click(self):
        Actions(self.driver).wait_and_click(By.XPATH, self.H6_BUTTON)

    def bold_text_click(self):
        Actions(self.driver).wait_and_click(By.XPATH, self.BOLD_TEXT)

    def italic_text_click(self):
        Actions(self.driver).wait_and_click(By.XPATH, self.ITALIC_TEXT)

    def strikethrough_text_click(self):
        Actions(self.driver).wait_and_click(By.XPATH, self.STRIKETHROUGH_TEXT)

    def underline_text_click(self):
        Actions(self.driver).wait_and_click(By.XPATH, self.UNDERLINE_TEXT)

    def quote_click(self):
        Actions(self.driver).wait_and_click(By.XPATH, self.QUOTE)

    def code_click(self):
        Actions(self.driver).wait_and_click(By.XPATH, self.CODE)

    def list_click(self):
        Actions(self.driver).wait_and_click(By.XPATH, self.LIST)

    def numbered_list_click(self):
        Actions(self.driver).wait_and_click(By.XPATH, self.NUMBERED_LIST)

    # def add_poll_checkbox_click(self):
    #     Actions(self.driver).click_to_element(By.XPATH, self.ADD_POLL_CHECKBOX)
    #
    # def add_additional_answer_click(self):
    #     Actions(self.driver).click_to_element(By.XPATH, self.ADD_OPTION_ANSWER)
    #
    # def delete_additional_answer_click(self):
    #     Actions(self.driver).click_to_element(By.XPATH, self.DELETE_OPTION_ANSWER)
    #
    # def forbid_comment_click(self):
    #     Actions(self.driver).click_to_element(By.XPATH, self.FORBID_COMMENT)
    #
    # # </Доступ по клику к элементам>

    # <Выделение текста>
    def select_main_text(self):
        Actions(self.driver).select_text(By.XPATH, self.MAIN_TEXT)
    # </Выделение текста>

    # def add_link_to_main_text(self, url, name):
    #     actions = Actions(self.driver)
    #     actions.click_to_element(By.XPATH, self.ADD_LINK_MAIN_TEXT)
    #     actions.wait_alert()
    #     actions.set_text_to_alert(url)
    #     actions.send_keys_and_perform(name)
    #
    # def insert_image_to_main_text(self, url, name=''):
    #     actions = Actions(self.driver)
    #     actions.click_to_element(By.XPATH, self.INSERT_IMG_MAIN_TEXT)
    #     actions.wait_alert()
    #     actions.set_text_to_alert(url)
    #     actions.send_keys_and_perform(name)
    #
    # def upload_image_to_main_text(self, path_to_file):
    #     actions = Actions(self.driver)
    #     actions.execute_script(self.SHOW_UPLOAD_PHOTO_CONTAINER_SCRIPT)
    #     actions.wait_until_elem_is_not_displayed(By.XPATH, self.INPUT_FILEDATA_MAIN_TEXT)
    #     actions.send_keys_to_elem_and_perform(By.XPATH, self.INPUT_FILEDATA_MAIN_TEXT, path_to_file)
    #     actions.wait_until_text_is_not_empty(By.XPATH, self.MAIN_TEXT)
    #
    # def add_poll(self, question, *answers):
    #     actions = Actions(self.driver)
    #     actions.click_to_element(By.XPATH, self.ADD_POLL_CHECKBOX)
    #     actions.send_keys_to_elem_and_perform(By.XPATH, self.QUESTION_POLL, question)
    #
    #     count = len(answers)
    #     for index in range(count):
    #         answer_xpath = self.ANSWEAR_POLL.format(index)
    #         if not actions.element_is_exist(By.XPATH, answer_xpath):
    #             answer_xpath += '[2]'
    #             actions.click_and_wait(By.XPATH, self.ADD_OPTION_ANSWER, By.XPATH, answer_xpath)
    #         actions.send_keys_to_elem_and_perform(By.XPATH, answer_xpath, answers[index])
    #
    # def add_user_to_main_text(self, name):
    #     actions = Actions(self.driver)
    #     actions.click_and_wait(By.XPATH, self.ADD_USER_MAIN_TEXT, By.XPATH, self.SEARCH_USER_POPUP)
    #     self.driver.find_element_by_xpath(self.SEARCH_USER_POPUP).click()
    #     actions.send_keys_to_elem_and_perform(By.XPATH, self.SEARCH_USER_POPUP, name)
    #     choose_user = '//*[contains(text(), "' + name + '")]'
    #     actions.wait_and_click(By.XPATH, choose_user)
    #     actions.wait_until_text_is_not_empty(By.XPATH, self.SHORT_TEXT)
