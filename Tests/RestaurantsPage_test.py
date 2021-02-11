import pytest
from Config.TestData import TestData
from Pages.RestaurantsPage import RestaurantsPage


@pytest.mark.parametrize('restaurant', TestData.RESTAURANTS_COLLECTION, ids=TestData.LIST_OF_RESTAURANTS_NAMES)
class TestRestaurantsPage:

    @pytest.mark.restaurant
    def test_title(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])
        title = self.restaurant.get_title()

        assert title == restaurant['title']

    def test_logo_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert self.restaurant.is_visible(RestaurantsPage.LOGO)

    def test_dish_group_is_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert self.restaurant.is_visible(RestaurantsPage.DISH_GROUP)
        assert self.restaurant.is_visible(RestaurantsPage.RESTAURANT_IN_GROUP)
        assert self.restaurant.is_visible(RestaurantsPage.ALCOHOL)
        assert self.restaurant.is_visible(RestaurantsPage.DISH)

    def test_dish_alcohol_is_clickable(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert self.restaurant.is_clickable(RestaurantsPage.ALCOHOL)
        assert self.restaurant.is_clickable(RestaurantsPage.DISH)
        assert self.restaurant.is_clickable(RestaurantsPage.RESTAURANT_IN_GROUP)




