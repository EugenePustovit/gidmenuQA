from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def get_title(self):
        return self.driver.title

    def click_profile_icon(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header div[class$=mx-3] a"))).click()

    def send_keys(self):
        pass