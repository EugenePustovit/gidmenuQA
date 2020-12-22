from Pages.HomePage import HomePage

# for class Test should be the beginning
class TestHomePage:
# only test_ should be in the beginning
    def test_title(self):
        self.home_page = HomePage(self.driver)
        title = self.home_page.get_title()

        assert title == HomePage.TITLE
