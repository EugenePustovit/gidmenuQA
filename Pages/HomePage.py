from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Config.TestData import TestData as TD
from Pages.BasePage import BasePage


class HomePage(BasePage):

    TITLE = 'Гастрономический путеводитель'

    def __init__(self, driver):
        super().__init__(driver)
        self.page_url = TD.HOME_PAGE_URL
        self.wait = WebDriverWait(self.driver, 10)

    def go_to_page(self):
        self.driver.get(self.page_url)

    def enter_email(self, text):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#inputLoginEmail"))).send_keys(text)

    def enter_password(self, text):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#inputPassword"))).send_keys(text)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    def get_login_error_message(self):
        modal_error_message_we = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#infoMsgModal div.modal-body")))
        print("Element: ' {element}'".format(element=modal_error_message_we))
        # print(type(modal_message_we))
        error_message = modal_error_message_we.text
        # print(error_message)
        return error_message