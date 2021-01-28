from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ErrorModal:

    ERROR_MODAL = (By.ID, "infoMsgModal")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div#infoMsgModal div.modal-body")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def get_error_message(self):
        error_str = self.driver.find_element(self.ERROR_MESSAGE[0], self.ERROR_MESSAGE[1]).text
        return error_str
