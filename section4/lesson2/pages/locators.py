from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//div[contains(@class, "basket-mini")]/span/a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM_LOCATOR = (By.ID, 'login_form')
    LOGIN_EMAIL_LOCATOR = (By.ID, 'id_login-username')
    LOGIN_PASSWORD_LOCATOR = (By.ID, 'id_login-password')
    LOGIN_SUBMIT_BTN_LOCATOR = (By.NAME, 'login_submit')

    REGISTRATION_FORM_LOCATOR = (By.ID, 'register_form')
    REGISTRATION_EMAIL_LOCATOR = (By.ID, 'id_registration-email')
    REGISTRATION_PASSWORD_LOCATOR = (By.ID, 'id_registration-password1')
    REGISTRATION_CONFIRM_PWD_LOCATOR = (By.ID, 'id_registration-password2')
    REGISTRATION_SUBMIT_BTN_LOCATOR = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_BASKET_BUTTON_LOCATOR = (By.CLASS_NAME, 'btn-add-to-basket')
    ADDED_PRODUCT_NAME_LOCATOR = (By.XPATH, "//div[@class='alertinner ']/strong[1]")
    BASKET_VALUE_LOCATOR = (By.XPATH, "//div[@class='alertinner ']/p/strong")
    PRODUCT_NAME_LOCATOR = (By.CSS_SELECTOR, '.product_main>h1')
    PRODUCT_COST_LOCATOR = (By.CSS_SELECTOR, '.product_main>.price_color')


class BasketPageLocators:
    BASKET_TITLE_LOCATOR = (By.CLASS_NAME, 'basket-title')
    BASKET_ITEMS_LOCATOR = (By.CLASS_NAME, 'basket-items')
    EMPTY_BASKET_LOCATOR = (By.XPATH, '//div[@class="content"]/div[@id="content_inner"]/p')
