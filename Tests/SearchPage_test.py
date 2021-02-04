import time
from Pages.SearchPage import SearchPage


class TestSearchPage:

    def test_search_filed_without_entering_dish_name(self):
        self.search_page = SearchPage(self.driver)
        self.search_page.click(SearchPage.SEARCH_BTN)
        current_text = self.search_page.text_from_web_page(SearchPage.LOCATOR_NO_RESULTS_FOR_SEARCH_DISHES)
        current_url = self.driver.current_url

        assert SearchPage.URL_NO_RESULTS == current_url
        assert SearchPage.TEXT_NO_RESULTS_FOR_SEARCH_DISHES == current_text

    def test_amount_of_elements_in_search_dropdown_list(self):
        self.search_page = SearchPage(self.driver)
        self.search_page.send_key(SearchPage.SEARCH_FILED, SearchPage.DISH_NAME)
        current_amount_of_elements = self.search_page.amount_Elements_in_Dropdown()

        assert current_amount_of_elements == SearchPage.DROPDOWN_ELEMENTS_AMOUNT

    def test_search_filed_with_entering_dish_name(self):
        self.search_page = SearchPage(self.driver)
        self.search_page.send_key(SearchPage.SEARCH_FILED, SearchPage.DISH_NAME)
        time.sleep(.2)
        self.search_page.click(SearchPage.SEARCH_BTN)
        current_text_no_restaurants_found = self.search_page.text_from_web_page(SearchPage.TEXT_NO_RESTAURANTS_FOUND)
        current_dish_in_result_page = self.search_page.text_from_web_page(SearchPage.DISH_FROM_DROPDOWN_IN_RESULTS_PAGE)

        assert current_dish_in_result_page == SearchPage.DISH_NAME_FROM_SEARCH_RESULT
        assert current_text_no_restaurants_found == SearchPage.TEXT_NO_RESULTS_FOR_SEARCH_RESTAURANTS

    def test_title_for_searched_dish_from_dropdown_list(self):
        self.search_page = SearchPage(self.driver)
        self.search_page.send_key(SearchPage.SEARCH_FILED, SearchPage.DISH_NAME)
        self.search_page.click(SearchPage.DISH_FROM_DROPDOWN_LIST)
        title = self.search_page.get_title()

        assert SearchPage.TITLE_RESULT_PAGE_DISH_FROM_DROPDOWN == title

        self.driver.get_screenshot_as_file('screen.png')
