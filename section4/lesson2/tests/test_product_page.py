import pytest

from section4.lesson2.pages.login_page import LoginPage
from section4.lesson2.pages.product_page import ProductPage
from section4.lesson2.pages.locators import ProductPageLocators
from section4.lesson2.tests.links import Links


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
                                      , marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_add_product_to_basket(browser, link):
    print(f'Go to {link}')
    product_page = ProductPage(browser, link)
    product_page.open()

    product_name = product_page.get_product_name()
    product_cost = product_page.get_product_cost()

    product_page.is_element_present(*ProductPageLocators.ADD_BASKET_BUTTON_LOCATOR)
    product_page.add_product_to_basket()
    product_page.solve_quiz_and_get_code()
    product_page.check_added_product(product_name, product_cost)


@pytest.mark.parametrize('link', [Links.NEW_YEAR_LINK])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_messages()


@pytest.mark.parametrize('link', [Links.NEW_YEAR_LINK])
def test_guest_cant_see_success_message(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_messages()


@pytest.mark.parametrize('link', [Links.NEW_YEAR_LINK])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_be_disappeared_success_msg()


@pytest.mark.parametrize('link', [Links.CITY_AND_STARS_LINK])
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', [Links.CITY_AND_STARS_LINK])
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_form()
