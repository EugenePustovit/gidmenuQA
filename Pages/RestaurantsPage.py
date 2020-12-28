from Pages.BasePage import BasePage


class PatriarshiePrudy(BasePage):

    PATRIARSHIE_PRUDY_URL = "https://gidmenu.com/restaurants/patriarshie-prudy/?show_dish_rest_groups=N"
    TITLE = "Патриаршие Пруды"

    def __init__(self, driver):
        super().__init__(driver)

        self.driver.get(PatriarshiePrudy.PATRIARSHIE_PRUDY_URL)
