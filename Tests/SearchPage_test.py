import pytest
from Config.TestData import TestData
from Pages.BasePage import is_visible, BasePage
from Pages.SearchPage import SearchPage


@pytest.mark.parametrize('findsearch', TestData.RESTAURANTS_COLLECTION, ids=TestData.LIST_OF_RESTAURANTS_NAMES)
class TestSearch:
    def test_find_search_field(self,findsearch):
        self.findsearch = SearchPage(self.driver, findsearch['url'])
        assert BasePage.is_visible(SearchPage.search) == True

    def





