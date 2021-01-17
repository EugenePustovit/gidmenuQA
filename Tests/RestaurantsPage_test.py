import pytest
from selenium.webdriver.common.by import By
from Config.TestData import TestData
from Pages.BasePage import BasePageDef
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

        assert BasePageDef(self.driver).is_visible(RestaurantsPage.LOGO) == True

    def test_dish_group_is_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(RestaurantsPage.DISH_GROUP) == True

    def test_dish_alcohol_is_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(RestaurantsPage.ALCOHOL) == True

    def test_dish_alcohol_is_clickable(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_clickable(RestaurantsPage.ALCOHOL) == True

    def test_dish_dish_is_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(RestaurantsPage.DISH) == True

    def test_dish_dish_is_clickable(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_clickable(RestaurantsPage.DISH) == True

    def test_dish_restaurants_group_is_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(RestaurantsPage.RESTAURANT_IN_GROUP) == True

    def test_dish_restaurants_group_is_clickable(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_clickable(RestaurantsPage.RESTAURANT_IN_GROUP) == True
