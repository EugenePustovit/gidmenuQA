import pytest

from Pages.BasePage import BasePage
from Pages.HomePage import HomePage
from Config.TestData import TestData as TD


class TestLogin:

    @pytest.mark.login
    def test_Login_invalid_password(self):

        self.driver.implicitly_wait(0)
        self.home_page = HomePage(self.driver)

        self.home_page.go_to_page()
        self.home_page.click_profile_icon()
        self.home_page.enter_email(TD.ACCOUNT['email'])
        self.home_page.enter_password(TD.ACCOUNT['invalid_password'])
        self.home_page.click_login()

        assert self.home_page.is_login_error_modal_displayed() == True
        assert self.home_page.get_login_error_message() == BasePage.LOGIN_ERROR_MESSAGE
