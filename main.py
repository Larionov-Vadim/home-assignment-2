# coding: utf-8

from selenium import webdriver
from create_topic_page import CreateTopicPage
from main_page import MainPage
import os
from selenium.webdriver.support.select import Select

login = "ftest3@tech-mail.ru"
passwd = "Pa$$w0rD-3"


# .//*[@id='header']/*[@class="login-button"]/*[@class='button2 button3 button-login trigger-login']

def main():
    print "Hello!"
    driver = webdriver.Firefox()
    page = MainPage(driver)
    page.open_page()
    page.login()

    topic_page = page.create_topic()
    topic_page.click_bold_bth_short_text()
    topic_page.click_italic_bth_text()
    topic_page.click_list_btn_short_text()
    topic_page.click_quote_btn_text()
    topic_page.submit()

    print "Yo!"


if __name__ == '__main__':
    main()