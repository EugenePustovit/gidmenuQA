from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import _element_if_visible, _find_element


class moving_is_finished_for_element_located(object):

    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element =  _element_if_visible(_find_element(driver, self.locator))
            if element:
                location = element.location
                sleep(.2)
                if element.location == location:
                    return element
            else: return False
        except NoSuchElementException:
            return False
