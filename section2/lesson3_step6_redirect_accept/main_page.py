from selenium.webdriver.common.by import By
from base_page import BasePage
from redirect_page import RedirectPage


class MainPage(BasePage):
    trollfaceSelector = (By.CSS_SELECTOR, '.trollface.btn')

    def go_to_next_page(self):
        trollface_btn = self.driver.find_element(*self.trollfaceSelector)
        trollface_btn.click()
        redirect_page = self.driver.window_handles[1]
        self.driver.switch_to.window(redirect_page)
        return RedirectPage(self.driver)
