import pytest

from section4.lesson2.pages.basket_page import BasketPage
from section4.lesson2.pages.main_page import MainPage
from section4.lesson2.tests.links import Links


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, Links.MAIN_PAGE_LINK)
        page.open()
        page.should_be_login_link()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        page = MainPage(browser, Links.MAIN_PAGE_LINK)
        page.open()
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.should_be_empty_basket()
        basket_page.should_be_message_for_empty_basket()
