from Pages.BasePage import BasePage


class RestaurantsPage(BasePage):

    def __init__(self, driver, url):
        super().__init__(driver)

        self.driver.get(url)
