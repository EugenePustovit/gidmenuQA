from selenium.webdriver.common.by import By

from Pages.Page import Page
from Pages.HomePage import HomePage
from Pages.ErrorModal import ErrorModal


class LoginPage(Page):

    INPUT_LOGIN = (By.CSS_SELECTOR, "input#inputLoginEmail")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input#inputPassword")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)
        HomePage(self.driver).go_to_page().click_profile_icon()

    def enter_email(self, text):
        self.driver.find_element(self.INPUT_LOGIN[0], self.INPUT_LOGIN[1]).send_keys(text)
        return self

    def enter_password(self, text):
        self.driver.find_element(self.INPUT_PASSWORD[0], self.INPUT_PASSWORD[1]).send_keys(text)
        return self

    def click_login(self):
        self.driver.find_element(self.LOGIN_BUTTON[0], self.LOGIN_BUTTON[1]).click()
        return HomePage(self.driver)

    def click_login_error_expected(self):
        self.driver.find_element(self.LOGIN_BUTTON[0], self.LOGIN_BUTTON[1]).click()
        return ErrorModal(self.driver)
