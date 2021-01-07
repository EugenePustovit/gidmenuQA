from Pages.BasePage import BasePage as BP
from Pages.RestaurantsPage import PatriarshiePrudy

class TestRestaurantsPagePatriarshiePrudy:

    def test_title(self):
        self.patriarshie_prudy = PatriarshiePrudy(self.driver)
        title = self.patriarshie_prudy.get_title()

        assert title == PatriarshiePrudy.TITLE