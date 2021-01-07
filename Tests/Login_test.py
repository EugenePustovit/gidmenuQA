from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from Pages.HomePage import HomePage


class TestLogin:

    def test_Login_invalid_password(self):

        self.home_page = HomePage(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

        self.home_page.go_to_page()
        self.home_page.click_profile_icon()
        self.home_page.enter_email("john.doe@mail.com")
        self.home_page.enter_password("Hilton102")
        self.home_page.click_login()
        sleep(3)
        modal_error_message_we = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#infoMsgModal div.modal-body")))
        print("Element: {element}".format(element=modal_error_message_we))
        error_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#infoMsgModal div.modal-body"))).text
        print("Error message test_login: '{element}'".format(element=error_message))
        err_msg = self.home_page.get_login_error_message
        print('Error message: {text}'.format(text=err_msg))
        sleep(3)
        assert err_msg.text == 'Неверный логин или пароль.'
