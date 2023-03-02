import pytest

from section4.lesson2.pages.login_page import LoginPage
from section4.lesson2.pages.main_page import MainPage
from section4.lesson2.tests.links import Links


def login_page(browser, url):
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()
    return LoginPage(browser, browser.current_url)


def test_should_be_present_login_form(browser):
    login_pg = login_page(browser, Links.SELENIUM_LINK)
    login_pg.should_be_login_form()


def test_should_be_present_registration_form(browser):
    login_pg = login_page(browser, Links.SELENIUM_LINK)
    login_pg.should_be_register_form()


def test_should_be_login_url(browser):
    login_pg = login_page(browser, Links.SELENIUM_LINK)
    login_pg.should_be_login_url()
