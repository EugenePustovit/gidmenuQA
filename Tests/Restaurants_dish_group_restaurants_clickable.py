import pytest
from selenium.webdriver.common.by import By
from Config import TestData
from Pages.RestaurantsPage import RestaurantsPage
from Pages.BasePage import BasePage


class TestRestaurantsPage:
    restaurants_group = (By.XPATH, '//*[@id="comp_2eb847c21003b7cf63dc43cd7faf48dd"]/div[1]/div/div[1]/a')

    @pytest.mark.parametrize('restaurant', TestData.RESTAURANTS_COLLECTION, ids=TestData.LIST_OF_RESTAURANTS_NAMES)
    def test_dish_restaurants_group_is_clickable(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePage(self.driver).click(self.restaurants_group) == True


















