# coding: utf-8
import urlparse
import config

from pages.auth import AuthForm, TopMenu


class Page(object):
    BASE_URL = 'http://ftest.stud.tech-mail.ru'
    PATH = ''

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()

    def close(self):
        self.driver.quit()

    def login(self):
        auth_form = AuthForm(self.driver)
        auth_form.open_form()
        auth_form.set_login(config.USEREMAIL)
        auth_form.set_password(config.PASSWORD)
        auth_form.submit()

    def find_username(self):
        return TopMenu(self.driver).get_username()