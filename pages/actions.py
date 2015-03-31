# coding: utf-8
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from component import Component

import conf

__author__ = 'vadim'


class Actions(Component):
    def select_text(self, by=By.XPATH, value=None):
        ActionChains(self.driver).\
            click(self.driver.find_element(by, value)).\
            key_down(Keys.CONTROL).\
            send_keys("a").\
            key_up(Keys.CONTROL).\
            perform()

    def set_text_to_alert(self, text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def click_to_element(self, by=By.XPATH, value=None):
        self.driver.find_element(by, value).click()

    def wait_alert(self):
        WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).\
            until(expected_conditions.alert_is_present())

    def send_keys_and_perform(self, *keys):
        ActionChains(self.driver).send_keys(*keys).perform()

    def wait_and_get_text(self, by=By.XPATH, value=None):
        return WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            lambda d: d.find_element(by, value).text
        )

    def wait_and_get_attribute(self, by=By.XPATH, value=None, attr=None):
        return WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            lambda d: d.find_element(by, value).get_attribute(attr)
        )