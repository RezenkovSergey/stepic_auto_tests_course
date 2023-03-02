import time

import pytest

from section4.lesson2.pages.product_page import ProductPage
from section4.lesson2.pages.locators import ProductPageLocators
from section4.lesson2.tests.links import Links


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
