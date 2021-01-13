import pytest
from selenium.webdriver.common.by import By
from Config import TestData
from Pages.RestaurantsPage import RestaurantsPage
from Pages.BasePage import BasePage


class TestRestaurantsPage:
    logo = (By.XPATH, '/html/body/div[2]')
    @pytest.mark.parametrize('restaurant', TestData.RESTAURANTS_COLLECTION, ids=TestData.LIST_OF_RESTAURANTS_NAMES)
    def test_logo_is_visible(self, restaurant):

        self.restaurant = RestaurantsPage(self.driver, restaurant['url'])

        assert BasePage(self.driver).is_visible(self.logo) ==True









        


