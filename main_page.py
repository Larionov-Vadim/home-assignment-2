# coding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from create_topic_page import CreateTopicPage


class MainPage(object):
    login_btn_xpath    = ".//*[@id='header']/p[3]/a"
    login_field_xpath  = ".//*[@id='popup-login-form']/div/p[1]/input"
    passwd_field_xpath = ".//*[@id='popup-login-form']/div/p[2]/input"
    submit_xpath       = ".//*[@id='popup-login-form-submit']"
    timeout = 10

    create_btn_xpath   = ".//*[@id='modal_write_show']"
    select_topic_xpath = ".//*[@id='modal_write']/div/ul/li[2]/a[2]"

    def __init__(self, driver):
        self.webdriver = driver
        self.url = 'http://ftest.stud.tech-mail.ru/'

    def open_page(self):
        self.webdriver.get(self.url)

    def close_page(self):
        self.webdriver.quit()

    def login(self):
        driver = self.webdriver

        login_btn = WebDriverWait(driver, self.timeout).\
            until(lambda driver: driver.find_element(By.XPATH, self.login_btn_xpath))
        login_btn.click()

        login_field_elem = WebDriverWait(driver, self.timeout).\
            until(lambda driver: driver.find_element(By.XPATH, self.login_field_xpath))
        passwd_field_elem = WebDriverWait(driver, self.timeout).\
            until(lambda driver: driver.find_element(By.XPATH, self.passwd_field_xpath))
        submit_btn = WebDriverWait(driver, self.timeout).\
            until(lambda driver: driver.find_element(By.XPATH, self.submit_xpath))


        login_field_elem.clear()
        login_field_elem.send_keys("ftest3@tech-mail.ru")
        passwd_field_elem.clear()
        passwd_field_elem.send_keys("Pa$$w0rD-3")
        submit_btn.submit()
        # Проверить, что действительно залогинился, иначе кинуть эксепшен
        return self

    def create_topic(self):
        driver = self.webdriver

        create_btn = WebDriverWait(driver, self.timeout).\
            until(lambda driver: driver.find_element(By.XPATH, self.create_btn_xpath))
        create_btn.click()

        select_topic_link = WebDriverWait(driver, self.timeout).\
            until(lambda driver: driver.find_element(By.XPATH, self.select_topic_xpath))
        select_topic_link.click()

        topic_page = CreateTopicPage(driver)
        return topic_page