from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from TestUtils.TestHelper import moving_is_finished_for_element_located
from Pages.Page import Page
from Pages.ErrorModal import ErrorModal


class LoginPage(Page):

    LOGIN_MODAL = (By.CSS_SELECTOR, "div#loginModal")
    INPUT_LOGIN = (By.CSS_SELECTOR, "input#inputLoginEmail")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input#inputPassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        self.driver = driver

    def is_focus_on_login_modal(self):
        self.wait.until(moving_is_finished_for_element_located(self.LOGIN_BUTTON))
        login_modal = self.wait.until(EC.visibility_of_element_located(self.LOGIN_MODAL))
        return login_modal == self.driver.switch_to.active_element

    def enter_email(self, text):
        self.driver.find_element(self.INPUT_LOGIN[0], self.INPUT_LOGIN[1]).send_keys(text)
        return self

    def enter_password(self, text):
        self.driver.find_element(self.INPUT_PASSWORD[0], self.INPUT_PASSWORD[1]).send_keys(text)
        return self

    def __get_login_button(self):
        return self.driver.find_element(self.LOGIN_BUTTON[0], self.LOGIN_BUTTON[1])

    def click_login_button(self):
        self.__get_login_button().click()

    def click_login_button_error_expected(self):
        self.__get_login_button().click()
        return ErrorModal(self.driver)
