from Config.TestData import TestData as TD
from Pages.BasePage import BasePage


class HomePage(BasePage):

    TITLE = 'Гастрономический путеводитель'

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)
        self.page_url = TD.HOME_PAGE_URL
