from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout= timeout

    def get_title(self):
        return self.driver.title

    def is_visible(self, by_locator):
        condition = EC.visibility_of_element_located(by_locator)
        element= WebDriverWait(self.driver, self.timeout).until(condition)

        return bool(element)

    def click(self, by_locator):
        condition= EC.visibility_of_element_located(by_locator)
        element = WebDriverWait(self.driver, self.timeout).until(condition)
        element.click()

        return bool(element)



