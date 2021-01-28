from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Pages.Page import Page


class BasePage(Page):

    PROFILE_ICON = (By.CSS_SELECTOR, "header div[class$=mx-3] a")

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.page_url = str()
        self.driver = driver

    def is_visible(self):
        condition = EC.visibility_of_element_located(self)
        return bool(condition)

    def is_clickable(self):
        condition = EC.element_to_be_clickable(self)
        return bool(condition)

    def go_to_page(self):
        self.driver.get(self.page_url)
        return self

    def click_profile_icon(self):
        self.driver.find_element(self.PROFILE_ICON[0], self.PROFILE_ICON[1]).click()
