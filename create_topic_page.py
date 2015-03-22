# coding: utf-8
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver


class CreateTopicPage(object):
    select_blog_xpath = ".//*[@id='id_blog']"
    timeout = 10

    title_xpath      = ".//*[@id='id_title']"
    short_text_xpath = ".//*[@id='content']/div/div[1]/form/div/div[3]/div[6]/div[1]/div/div/div/div[3]/pre"
    text_xpath       = ".//*[@id='content']/div/div[1]/form/div/div[6]/div[6]/div[1]/div/div/div/div[3]/pre"

    bold_btn_short_text_xpath = ".//*[@id='content']/div/div[1]/form/div/div[2]/a[1]"
    bold_btn_text_xpath       = ".//*[@id='content']/div/div[1]/form/div/div[5]/a[1]"

    italic_btn_short_text_xpath = ".//*[@id='content']/div/div[1]/form/div/div[2]/a[2]"
    italic_btn_text_xpath       = ".//*[@id='content']/div/div[1]/form/div/div[5]/a[2]"

    quote_btn_short_text_xpath = ".//*[@id='content']/div/div[1]/form/div/div[2]/a[3]"
    quote_btn_text_xpath       = ".//*[@id='content']/div/div[1]/form/div/div[5]/a[3]"

    list_btn_short_text_xpath = ".//*[@id='content']/div/div[1]/form/div/div[2]/a[5]"
    list_btn_text_xpath       = ".//*[@id='content']/div/div[1]/form/div/div[5]/a[5]"

    insert_link_btn_short_text_xpath = ".//*[@id='content']/div/div[1]/form/div/div[2]/a[6]"
    insert_link_btn_text_xpath       = ".//*[@id='content']/div/div[1]/form/div/div[5]/a[6]"

    insert_img_btn_short_text_xpath = ".//*[@id='content']/div/div[1]/form/div/div[2]/a[7]"
    insert_img_btn_text_xpath       = ".//*[@id='content']/div/div[1]/form/div/div[5]/a[7]"

    upload_img_btn_short_text_xpath = ".//*[@id='content']/div/div[1]/form/div/div[2]/a[8]"
    upload_img_btn_text_xpath       = ".//*[@id='content']/div/div[1]/form/div/div[5]/a[8]"

    add_user_btn_short_text_xpath = ".//*[@id='content']/div/div[1]/form/div/div[2]/a[9]"
    add_user_btn_text_xpath       = ".//*[@id='content']/div/div[1]/form/div/div[5]/a[9]"

    submit_btn_xpath = ".//*[@id='content']/div/div[1]/form/div/button"

    title = "Тестовый заговок"
    short_text = "Тестовый короткий текст"
    text = "Основной текст, тест"

    def __init__(self, webdriver):
        self.driver = webdriver

    def select_blog(self, item):
        driver = self.driver
        select_blog_dropdown_elem = WebDriverWait(driver, self.timeout).\
            until(lambda driver: driver.find_element_by_xpath(self.select_blog_xpath))
        Select(select_blog_dropdown_elem).select_by_index(1)
        return self


    def set_title(self, msg=title):
        driver = self.driver
        title_field = WebDriverWait(driver, self.timeout).\
            until(lambda driver: driver.find_element_by_xpath(self.title_xpath))
        title_field.send_keys('TITLE')

    def set_short_text(self, msg=short_text):
        driver = self.driver
        short_text_field = WebDriverWait(driver, self.timeout).\
            until(lambda driver: driver.find_element_by_xpath(self.short_text_xpath))

        print short_text_field
        short_text_field.send_keys(msg)


    def set_text(self, msg=text):
        driver = self.driver
        text_field = WebDriverWait(driver, self.timeout).\
            until(lambda driver: driver.find_element(By.XPATH, self.text_xpath))
        print("%(")
        text_field.send_keys('Yo!')

    def close_page(self):
        self.driver.quit()

    def get_blog_xpath_by_id(self, id_blog):
        if id_blog < 0:
            raise ValueError
        return ".//*[@id='id_blog_chzn_o_{id_blog}']".format(id_blog=id_blog)


    def click_bold_bth_short_text(self):
        driver = self.driver
        bold_btn = driver.find_element_by_xpath(self.bold_btn_short_text_xpath)
        bold_btn.click()

    def click_bold_bth_text(self):
        driver = self.driver
        bold_btn = driver.find_element_by_xpath(self.bold_btn_text_xpath)
        bold_btn.click()


    def click_italic_bth_short_text(self):
        driver = self.driver
        italic_btn = driver.find_element_by_xpath(self.italic_btn_short_text_xpath)
        italic_btn.click()

    def click_italic_bth_text(self):
        driver = self.driver
        italic_btn = driver.find_element_by_xpath(self.italic_btn_text_xpath)
        italic_btn.click()


    def click_quote_btn_short_text(self):
        driver = self.driver
        quote_btn = driver.find_element_by_xpath(self.quote_btn_short_text_xpath)
        quote_btn.click()

    def click_quote_btn_text(self):
        driver = self.driver
        quote_btn = driver.find_element_by_xpath(self.quote_btn_text_xpath)
        quote_btn.click()


    def click_list_btn_short_text(self):
        driver = self.driver
        list_btn = driver.find_element_by_xpath(self.list_btn_short_text_xpath)
        list_btn.click()

    def click_list_btn_text(self):
        driver = self.driver
        list_btn = driver.find_element_by_xpath(self.list_btn_text_xpath)
        list_btn.click()

    def submit(self):
        driver = self.driver
        submit_btn = driver.find_element_by_xpath(self.submit_btn_xpath)
        submit_btn.click()
