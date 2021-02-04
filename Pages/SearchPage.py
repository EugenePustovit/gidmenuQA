from selenium.webdriver.common.by import By
from Config.TestData import TestData as TD
from Pages.BasePage import BasePage


class SearchPage(BasePage):
    SEARCH_FILED = (By.XPATH, '//*[@id="smart-title-search-input"]')
    LOCATOR_NO_RESULTS_FOR_SEARCH_DISHES = (By.XPATH, '/html/body/div[2]/div/div[1]/main/div/div/p')
    TEXT_NO_RESULTS_FOR_SEARCH_DISHES = 'Пожалуйста, введите поисковую фразу'
    SEARCH_BTN = (By.NAME, 's')
    DISH_NAME = 'блины'
    DISH_FROM_DROPDOWN_LIST = (By.XPATH, '/html/body/div[6]/div/a[1]')
    DISH_FROM_DROPDOWN_IN_RESULTS_PAGE = (By.XPATH, '//*[@id="bx_2169441148_272670_1e8aca5f6204f540293dfcb5f04bc241"]/div/div[1]/div[1]/div[2]/div/div/div[1]/div/a/h6')
    LIST_OF_DISHES_IN_DROPDOWN = (By.XPATH, '/html/body/div[6]/div/a')
    DROPDOWN_ELEMENTS_AMOUNT = 30
    TEXT_NO_RESTAURANTS_FOUND = (By.XPATH , '//*[@id="search-block"]/div/div[1]/main/div/div/p/font')
    TEXT_NO_RESULTS_FOR_SEARCH_RESTAURANTS= 'К сожалению, на ваш поисковый запрос ничего не найдено.'
    DISH_NAME_FROM_SEARCH_RESULT = 'Блины с сыром и ветчиной'
    URL_NO_RESULTS = 'https://gidmenu.com/search/?q=&s='
    TITLE_RESULT_PAGE_DISH_FROM_DROPDOWN = 'Завтраки в Золотая вобла, Блины с сыром и ветчиной'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TD.HOME_PAGE_URL)

    def amount_Elements_in_Dropdown(self):
        elements_in_dropdown = self.driver.find_elements(*SearchPage.LIST_OF_DISHES_IN_DROPDOWN)
        amount_elements_in_dropdown = len(elements_in_dropdown)

        return amount_elements_in_dropdown



