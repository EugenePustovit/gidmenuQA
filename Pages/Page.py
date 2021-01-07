from selenium.webdriver.support.wait import WebDriverWait


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def get_title(self):
        return self.driver.title