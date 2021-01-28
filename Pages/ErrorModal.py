from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ErrorModal:

    ERROR_MODAL = (By.ID, "infoMsgModal")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div#infoMsgModal div.modal-body")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 3)

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MODAL)).text
