import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

REMOTE_URL = 'http://127.0.0.1:4444/wd/hub'


def init_remote_driver_chrome():
    caps = DesiredCapabilities.CHROME.copy()

    driver = webdriver.Remote(command_executor=REMOTE_URL,
                              desired_capabilities=caps)

    return driver


def init_remote_driver_firefox():
    caps = DesiredCapabilities.FIREFOX.copy()

    driver = webdriver.Remote(command_executor=REMOTE_URL,
                              desired_capabilities=caps)

    return driver


@pytest.fixture(params=['chrome', 'firefox'], scope='class', autouse=True)
def init_driver(request):
    driver = None
    if request.param == 'chrome':
        driver = init_remote_driver_chrome()
    elif request.param == 'firefox':
        driver = init_remote_driver_firefox()
    else:
        print('Please pass the correct browser name: {}'.format(request.param))
        raise Exception('driver is not found')

    driver.implicitly_wait(5)
    request.cls.driver = driver

    yield

    driver.quit()
