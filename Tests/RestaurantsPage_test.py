import pytest
from selenium.webdriver.common.by import By
from Config.TestData import TestData
from Pages.BasePage import BasePageDef
from Pages.RestaurantsPage import RestaurantsPage


@pytest.mark.parametrize('restaurant', TestData.RESTAURANTS_COLLECTION, ids=TestData.LIST_OF_RESTAURANTS_NAMES)
class TestRestaurantsPage:
    logo = (By.XPATH, '/html/body/div[2]')
    dish_group = (By.XPATH, '//*[@id="comp_2eb847c21003b7cf63dc43cd7faf48dd"]/div[1]/div')
    alcohol = (By.XPATH, '//*[@id="comp_2eb847c21003b7cf63dc43cd7faf48dd"]/div[1]/div/div[3]/a')
    dish = (By.XPATH, '//*[@id="comp_2eb847c21003b7cf63dc43cd7faf48dd"]/div[1]/div/div[2]/a')
    restaurants_group = (By.XPATH, '//*[@id="comp_2eb847c21003b7cf63dc43cd7faf48dd"]/div[1]/div/div[1]/a')

    @pytest.mark.restaurant
    # test title for each restaurant page
    def test_title(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])
        title = self.restaurant.get_title()

        assert title == restaurant['title']

    # test logo  for each restaurant page
    def test_logo_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(self.logo) == True

    # test dish_group  filed  for each restaurant page
    def test_dish_group_is_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(self.dish_group) == True

    # test dish_group Alcohol is visible   for each restaurant page
    def test_dish_alcohol_is_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(self.alcohol) == True

    # test dish_group Alcohol is clickable    for each restaurant page
    def test_dish_alcohol_is_clickable(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(self.alcohol) == True

    # test dish_group Dish is visible  for each restaurant page
    def test_dish_dish_is_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(self.dish) == True

    # test dish_group Dish is clickable   for each restaurant page
    def test_dish_dish_is_clickable(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(self.dish) == True

    # test dish_group Restaurants  is visible  for each restaurant page
    def test_dish_restaurants_group_is_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(self.restaurants_group) == True

    # test dish_group Restaurants  is clickable   for each restaurant page
    def test_dish_restaurants_group_is_clickable(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePageDef(self.driver).is_visible(self.restaurants_group) == True
