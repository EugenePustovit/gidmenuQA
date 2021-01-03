from Pages.BreakfastPage import BreakfastPage


class TestHomePage:

    HOME_BUTTON = '//header//a[@class="navbar-brand"]'


    def test_title(self):
        self.breakfasts_page = BreakfastPage(self.driver)
        title = self.breakfasts_page.get_title()

        assert title == BreakfastPage.TITLE


