from section4.lesson2.pages.main_page import MainPage
from section4.lesson2.tests.links import Links


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, Links.MAIN_PAGE_LINK)
    page.open()
    page.should_be_login_link()
