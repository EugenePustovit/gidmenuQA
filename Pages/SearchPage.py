from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.TestData import TestData as TD


class SearchPage(BasePage):
    search = (By.ID, 'smart-title-search-input')

    def __init__(self, driver, url):
        super().__init__(driver)

        self.driver.get(TD.HOME_PAGE_URL)
