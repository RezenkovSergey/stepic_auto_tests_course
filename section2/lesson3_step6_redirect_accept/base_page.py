from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self,  driver: WebDriver, url: str):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def close(self):
        self.driver.close()


