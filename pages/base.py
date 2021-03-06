# coding: utf-8
import os
from selenium.webdriver.common.by import By
import conf
import urlparse
from component import Component
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import DesiredCapabilities, Remote
from selenium.webdriver.support import expected_conditions

__author__ = 'vadim'


class Page(object):
    BASE_URL = 'http://ftest.stud.tech-mail.ru'
    PATH = ''

    def __init__(self, driver=None):
        if driver is None:
            browser = os.environ.get('TTHA2BROWSER', 'CHROME')
            self.driver = Remote(
                command_executor='http://127.0.0.1:4444/wd/hub',
                desired_capabilities=getattr(DesiredCapabilities, browser)
            )
        else:
            self.driver = driver

    def get_driver(self):
        return self.driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def login(self):
        auth_form = AuthForm(self.driver)
        auth_form.open_form()
        auth_form.set_login(conf.USEREMAIL)
        auth_form.set_password(conf.PASSWORD)
        auth_form.submit()
        return self.find_username()

    def find_username(self):
        return TopMenu(self.driver).get_username()


class AuthForm(Component):
    LOGIN = '//input[@name="login"]'
    PASSWORD = '//input[@name="password"]'
    SUBMIT = '//span[text()="Войти"]'
    LOGIN_BUTTON = '//a[text()="Вход для участников"]'

    def open_form(self):
        WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.LOGIN_BUTTON))
        )
        self.driver.find_element_by_xpath(self.LOGIN_BUTTON).click()

    def set_login(self, login):
        WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.LOGIN))
        )
        self.driver.find_element_by_xpath(self.LOGIN).send_keys(login)

    def set_password(self, pwd):
        WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.PASSWORD))
        )
        self.driver.find_element_by_xpath(self.PASSWORD).send_keys(pwd)

    def submit(self):
        WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.SUBMIT))
        )
        self.driver.find_element_by_xpath(self.SUBMIT).click()


class TopMenu(Component):
    USERNAME = '//a[@class="username"]'

    def get_username(self):
        return WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            lambda d: d.find_element_by_xpath(self.USERNAME).text
        )
