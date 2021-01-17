from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class RestaurantsPage(BasePage):
    LOGO = (By.XPATH, '/html/body/div[2]')
    DISH_GROUP = (By.XPATH, '//*[@id="comp_2eb847c21003b7cf63dc43cd7faf48dd"]/div[1]/div')
    ALCOHOL = (By.XPATH, '//*[@id="comp_2eb847c21003b7cf63dc43cd7faf48dd"]/div[1]/div/div[3]/a')
    DISH = (By.XPATH, '//*[@id="comp_2eb847c21003b7cf63dc43cd7faf48dd"]/div[1]/div/div[2]/a')
    RESTAURANT_IN_GROUP = (By.XPATH, '//*[@id="comp_2eb847c21003b7cf63dc43cd7faf48dd"]/div[1]/div/div[1]/a')

    def __init__(self, driver, url):
        super().__init__(driver)

        self.driver.get(url)


