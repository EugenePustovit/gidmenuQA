from time import sleep
from Pages.HomePage import HomePage


class TestLogin:

    def test_Login_invalid_password(self):

        self.home_page = HomePage(self.driver)

        self.home_page.go_to_page()
        self.home_page.click_profile_icon()
        self.home_page.enter_email("john.doe@mail.com")
        self.home_page.enter_password("Hilton102")
        self.home_page.click_login()
        sleep(3)
        err_msg = self.home_page.get_login_error_message
        print('Error message:')
        print(err_msg)
        sleep(3)
        assert err_msg == 'Неверный логин или пароль.'
