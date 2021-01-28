import pytest

from Pages.LoginPage import LoginPage
from Config.TestData import TestData as TD


class TestLogin:

    @pytest.mark.login
    def test_login_invalid_password(self):

        assert LoginPage(self.driver)\
            .enter_email(TD.ACCOUNT['email'])\
            .enter_password(TD.ACCOUNT['invalid_password'])\
            .click_login_error_expected()\
            .get_error_message() == TD.LOGIN_ERROR_MESSAGE_TEXT
