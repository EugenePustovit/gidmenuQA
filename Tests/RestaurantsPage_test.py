import pytest
from Config.TestData import TestData
from Pages.RestaurantsPage import RestaurantsPage


class TestRestaurantsPage:

    @pytest.mark.parametrize('restaurant', TestData.RESTAURANTS_COLLECTION)
    def test_title(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])
        title = self.restaurant.get_title()

        assert title == restaurant['title']
