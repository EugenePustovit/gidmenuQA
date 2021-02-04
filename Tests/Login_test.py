import pytest

from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Config.TestData import TestData as TD


class TestLogin:

    @pytest.mark.login
    def test_login_invalid_password(self):

        home_page = HomePage(self.driver)
        home_page.go_to_page().click_profile_icon()
        login_page = LoginPage(self.driver)
        error_modal = login_page.enter_email(TD.ACCOUNT['email'])\
            .enter_password(TD.ACCOUNT['invalid_password'])\
            .click_login_button_error_expected()

        assert error_modal.is_focus_on_error_modal()
        assert error_modal.get_error_message() == TD.LOGIN_ERROR_MESSAGE_TEXT

        error_modal.close_error_modal()
        home_page.click_profile_icon()

        assert login_page.is_focus_on_login_modal()
