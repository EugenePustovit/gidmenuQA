from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.Page import Page


class BasePage(Page):
    LOGIN_ERROR_MESSAGE = 'Неверный логин или пароль.'

    def __init__(self, driver):
        super(BasePage, self).__init__(driver)
        self.page_url = str()
        self.driver = driver

    def text_from_web_page(self, locator):
        text_from_web = self.driver.find_element(*locator).text
        return text_from_web

    def is_visible(self, element):
        condition = EC.visibility_of_element_located(element)
        return bool(condition)

    def is_clickable(self, element):
        condition = EC.element_to_be_clickable(element)

        return bool(condition)

    def click(self, locator):
        element = self.driver.find_element(locator[0], locator[1])
        element.click()

    def send_key(self, locator, value):
        element = self.driver.find_element(locator[0], locator[1])
        element.send_keys(value)

    def go_to_page(self):
        self.driver.get(self.page_url)

    def click_profile_icon(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "header div[class$=mx-3] a"))).click()

    def enter_email(self, text):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#inputLoginEmail"))).send_keys(text)

    def enter_password(self, text):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input#inputPassword"))).send_keys(text)

    def click_login(self):
        self.driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    def is_login_error_modal_displayed(self):
        if self.wait.until(EC.visibility_of_element_located((By.ID, "infoMsgModal"))).is_displayed():
            return True
        else:
            return False

    def get_login_error_message(self):
        error_str = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div#infoMsgModal div.modal-body"))).text
        return error_str
