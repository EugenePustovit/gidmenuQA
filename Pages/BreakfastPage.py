from Config.TestData import TestData as TD
from Pages.BasePage import BasePage


class BreakfastPage(BasePage):

    TITLE = 'Завтраки'

    def __init__(self, driver):
        super().__init__(driver)

        self.driver.get(TD.BREAKFASTS_PAGE_URL)
