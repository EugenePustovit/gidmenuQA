import pytest
from selenium.webdriver.common.by import By
from Config import TestData
from Pages.RestaurantsPage import RestaurantsPage
from Pages.BasePage import BasePage


class TestRestaurantsPage:
    alcohol = (By.XPATH, '//*[@id="comp_2eb847c21003b7cf63dc43cd7faf48dd"]/div[1]/div/div[3]/a')

    @pytest.mark.parametrize('restaurant', TestData.RESTAURANTS_COLLECTION, ids=TestData.LIST_OF_RESTAURANTS_NAMES)
    def test_dish_alcohol_is_visible(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePage(self.driver).is_visible(self.alcohol) == True


















