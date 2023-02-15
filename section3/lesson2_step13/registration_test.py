import time
import unittest

from selenium import webdriver

from section3.lesson2_step13.registration_page import RegistrationPage


class RegistrationTest(unittest.TestCase):
    link_registration_fst = 'http://suninjuly.github.io/registration1.html'
    link_registration_scd = 'http://suninjuly.github.io/registration2.html'
    fst_name_str = 'Test'
    lst_name_str = 'Test'
    email_str = 'test@test.ru'
    expected_msg = 'Congratulations! You have successfully registered!'

    def test_registration_fst(self):
        driver = webdriver.Chrome()
        registration_page = RegistrationPage(driver, self.link_registration_fst)
        welcome_msg = registration_page.open()\
            .send_fst_name(self.fst_name_str)\
            .send_lst_name(self.lst_name_str)\
            .send_email(self.email_str)\
            .submit_form()
        time.sleep(10)
        registration_page.close()
        self.assertEqual(welcome_msg, self.expected_msg, f"Expected: {self.expected_msg}, got {welcome_msg}")

    def test_registration_scd(self):
        driver = webdriver.Chrome()
        registration_page = RegistrationPage(driver, self.link_registration_scd)
        welcome_msg = registration_page.open()\
            .send_fst_name(self.fst_name_str)\
            .send_lst_name(self.lst_name_str)\
            .send_email(self.email_str)\
            .submit_form()
        time.sleep(10)
        registration_page.close()
        self.assertEqual(welcome_msg, self.expected_msg, f"Expected: {self.expected_msg}, got {welcome_msg}")


if __name__ == '__main__':
    unittest.main()
