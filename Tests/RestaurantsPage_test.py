import pytest
from Config.TestData import TestData
from Pages.BasePage import BasePage
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

        assert BasePage.is_visible(RestaurantsPage.LOGO)

    def test_dish_group_is_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePage.is_visible(RestaurantsPage.DISH_GROUP)
        assert BasePage.is_visible(RestaurantsPage.RESTAURANT_IN_GROUP)
        assert BasePage.is_visible(RestaurantsPage.ALCOHOL)
        assert BasePage.is_visible(RestaurantsPage.DISH)

    def test_dish_alcohol_is_clickable(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePage.is_clickable(RestaurantsPage.ALCOHOL)
        assert BasePage.is_clickable(RestaurantsPage.DISH)
        assert BasePage.is_clickable(RestaurantsPage.RESTAURANT_IN_GROUP)


