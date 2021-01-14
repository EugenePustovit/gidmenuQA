class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title
