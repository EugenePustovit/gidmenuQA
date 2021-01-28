from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from TestUtils.TestHelper import moving_is_finished_for_element_located
from Pages.Page import Page


class ErrorModal(Page):

    ERROR_MODAL = (By.ID, "infoMsgModal")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div#infoMsgModal div.modal-body")

    def __init__(self, driver):
        super(ErrorModal, self).__init__(driver)
        self.driver = driver

    def is_focus_on_error_modal(self):
        self.wait.until(moving_is_finished_for_element_located(self.ERROR_MESSAGE))
        error_modal = self.wait.until(EC.visibility_of_element_located(self.ERROR_MODAL))
        return error_modal == self.driver.switch_to.active_element

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MODAL)).text

    def close_error_modal(self):
        error_message = self.wait.until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        ActionChains(self.driver).move_to_element_with_offset(error_message, -15, -15).click().perform()
        self.wait.until(EC.invisibility_of_element(error_message))
