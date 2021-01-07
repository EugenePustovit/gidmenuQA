from Pages.HomePage import HomePage


class TestHomePage:

    def test_title(self):

        self.home_page = HomePage(self.driver)

        self.home_page.go_to_page()
        assert self.home_page.get_title() == HomePage.TITLE
