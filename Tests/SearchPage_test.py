import pytest

from Config.TestData import TestData
from Pages.BasePage import BasePageDef


@pytest.mark.parametrize('restaurant', TestData.RESTAURANTS_COLLECTION, ids=TestData.LIST_OF_RESTAURANTS_NAMES)
class Search:
    def

