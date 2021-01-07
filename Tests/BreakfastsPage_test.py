from time import sleep

import pytest

from Config.TestData import TestData
from Pages.BreakfastPage import BreakfastPage


class TestBreakfastPage:

    HOME_BUTTON = '//header//a[@class="navbar-brand"]'

#    @pytest.mark.parametrize('restaurant', TestData.RESTAURANT_COLLECTION)
    def test_title(self):
        self.breakfasts_page = BreakfastPage(self.driver)
        title = self.breakfasts_page.get_title()

        assert title == BreakfastPage.TITLE
        sleep(5)

