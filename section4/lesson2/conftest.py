import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser(request):
    user_languages = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_languages})
    print('\nStart browser for test...')
    driver = webdriver.Chrome(options=options)
    yield driver
    print('\nQuit browser')
    driver.quit()


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help='Language for online shop')
