import pytest
from selenium.webdriver.common.by import By
from Config import TestData
from Pages.RestaurantsPage import RestaurantsPage
from Pages.BasePage import BasePage


class TestRestaurantsPage:
    dish = (By.XPATH, '//*[@id="comp_2eb847c21003b7cf63dc43cd7faf48dd"]/div[1]/div/div[2]/a')

    @pytest.mark.parametrize('restaurant', TestData.RESTAURANTS_COLLECTION, ids=TestData.LIST_OF_RESTAURANTS_NAMES)
    def test_dish_dish_is_clickable(self, restaurant):
        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePage(self.driver).click(self.dish) == True


















