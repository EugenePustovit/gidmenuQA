from Pages.HomePage import HomePage


class TestHomePage:

    def test_title(self):
        self.home_page = HomePage(self.driver)
        title = self.home_page.get_title()

        assert title == HomePage.TITLE