import math
import time

import pytest
from selenium import webdriver

from section3.lesson6_step4_login.main_page import MainPage


@pytest.fixture(scope='function')
def set_driver():
    print('\nStart browser for test ...')
    driver = webdriver.Firefox()
    yield driver
    print('\nQuit browser')
    driver.quit()


class TestCorrectAnswer:

    expected_text = 'Correct!'

    @pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                      'https://stepik.org/lesson/236896/step/1',
                                      'https://stepik.org/lesson/236897/step/1',
                                      'https://stepik.org/lesson/236898/step/1',
                                      'https://stepik.org/lesson/236899/step/1',
                                      'https://stepik.org/lesson/236903/step/1',
                                      'https://stepik.org/lesson/236904/step/1',
                                      'https://stepik.org/lesson/236905/step/1'])
    def test_correct_test_should_be(self, set_driver, link):
        main_page = MainPage(set_driver, link)
        main_page.open().go_to_login()\
            .send_email('email')\
            .send_password('password')\
            .click_login_btn()
        time.sleep(15)

        answer = str(math.log(int(time.time())))
        print('Answer: ', answer)
        main_page.send_answer(answer)\
            .submit_answer()
        time.sleep(10)
        actual_text = main_page.get_hint_text()
        assert actual_text == self.expected_text, f"Expected text: {self.expected_text}, got {actual_text}"
