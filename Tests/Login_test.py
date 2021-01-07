from Pages.BasePage import BasePage
from Pages.HomePage import HomePage


class TestLogin:

    def test_Login_invalid_password(self):

        self.driver.implicitly_wait(0)
        self.home_page = HomePage(self.driver)

        self.home_page.go_to_page()
        self.home_page.click_profile_icon()
        self.home_page.enter_email("john.doe@mail.com")
        self.home_page.enter_password("Hilton102")
        self.home_page.click_login()

        assert self.home_page.is_login_error_modal_displayed() == True
        assert self.home_page.get_login_error_message() == BasePage.LOGIN_ERROR_MESSAGE
