from Pages.BasePage import BasePage


class RestaurantsPage(BasePage):

    # PATRIARSHIE_PRUDY_URL = "https://gidmenu.com/restaurants/patriarshie-prudy/?show_dish_rest_groups=N"
    # TITLE = "Патриаршие Пруды"

    def __init__(self, driver, url):
        super().__init__(driver)

        self.driver.get(url)
