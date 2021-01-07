class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout =timeout

    def get_title(self):
        return self.driver.title
