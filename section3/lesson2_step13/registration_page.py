from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class RegistrationPage:

    fst_name_selector = (By.CSS_SELECTOR, 'input[required=""].first')
    lst_name_selector = (By.CSS_SELECTOR, 'input[required=""].second')
    email_selector = (By.CSS_SELECTOR, 'input[required=""].third')
    btn_selector = (By.CSS_SELECTOR, "button.btn")

    def __init__(self, driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    def send_fst_name(self, fst_name):
        fst_name_elt = self.driver.find_element(*self.fst_name_selector)
        fst_name_elt.send_keys(fst_name)
        return self

    def send_lst_name(self, lst_name):
        lst_name_elt = self.driver.find_element(*self.lst_name_selector)
        lst_name_elt.send_keys(lst_name)
        return self

    def send_email(self, email):
        email_elt = self.driver.find_element(*self.email_selector)
        email_elt.send_keys(email)
        return self

    def submit_form(self):
        btn_elt = self.driver.find_element(*self.btn_selector)
        btn_elt.click()

        welcome_text_elt = self.driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        return welcome_text

    def open(self):
        self.driver.get(self.url)
        return self

    def close(self):
        self.driver.quit()
