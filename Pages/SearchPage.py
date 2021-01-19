from Pages.BasePage import BasePage
from Config.TestData import TestData as TD


class Search(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver)

        self.driver.get(TD.HOME_PAGE_URL)
        