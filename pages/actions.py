# coding: utf-8
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from component import Component
import conf
from selenium import webdriver

__author__ = 'vadim'


class Actions(Component):
    def select_text(self, by=By.XPATH, value=None):
        ActionChains(self.driver).click(self.driver.find_element(by, value)).\
            key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

    def set_text_to_alert(self, text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def click_to_element(self, by=By.XPATH, value=None):
        self.driver.find_element(by, value).click()

    def wait_alert(self):
        WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).\
            until(expected_conditions.alert_is_present())

    def send_keys_to_elem_and_perform(self, by, name, *keys):
        elem = self.driver.find_element(by, name)
        ActionChains(self.driver).send_keys_to_element(elem, *keys).perform()

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

    def wait_until_text_is_not_empty(self, by, value):
        WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            lambda d: d.find_element(by, value).text != ''
        )

    def wait_until_execute_script_is_not_empty(self, script):
        return WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            lambda d: d.execute_script(script) != ''
        )

    def wait_until_execute_script_is_not_equals_msg(self, script, msg):
        return WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            lambda d: d.execute_script(script) != msg
        )

    def execute_script(self, script):
        self.driver.execute_script(script)

    def element_is_exist(self, by, value):
        try:
            self.driver.find_element(by, value)
            return True
        except NoSuchElementException:
            return False

    def click_and_wait(self, by_click, click_to, by_expectation, expectation):
        self.driver.find_element(by_click, click_to).click()
        WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            lambda d: d.find_element(by_expectation, expectation).is_displayed()
        )

    def get_list_elements(self, by, value):
        elements = list()
        index = 1
        try:
            while True:
                new_value = '(' + value + ')[' + str(index) + ']'
                elements.append(self.driver.find_element(by, new_value))
                index += 1
        except NoSuchElementException:
            return elements

    def get_list_text_from_list_elements(self, *elements):
        text_list = list()
        for x in elements:
            text_list.append(x.text)
        return text_list

    def submit(self, by=By.XPATH, value=None):
        self.driver.find_element(by, value).submit()

    def wait_and_click(self, by=By.XPATH, value=None):
        WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            lambda d: d.find_element(by, value).is_displayed()
        )
        self.driver.find_element(by, value).click()

    def get_text(self, by=By.XPATH, value=None):
        return self.driver.find_element(by, value).text

    def wait_until_elem_is_not_displayed(self, by, value):
        WebDriverWait(self.driver, conf.TIMEOUT, conf.POLL_FREQUENCY).until(
            lambda d: d.find_element(by, value).is_displayed()
        )

    def clear(self, by, value):
        self.driver.find_element(by, value).clear()