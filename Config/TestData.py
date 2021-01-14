class TestData:

    HOME_PAGE_URL = 'http://www.gidmenu.com'
    BREAKFASTS_PAGE_URL = HOME_PAGE_URL + '/restaurants/zavtraki/'

    PATRIARSHIE_PRUDY = {
        'url': 'https://gidmenu.com/restaurants/patriarshie-prudy/?show_dish_rest_groups=N',
        'title': 'Патриаршие Пруды'
    }

    RESTAURANT_COLLECTION = [PATRIARSHIE_PRUDY]
    ACCOUNT = {
        'email': 'john.doe@mail.com',
        'password': 'Hilton101',
        'invalid_email': 'john.doe@mail.con',
        'invalid_password': 'Hilton102'
    }
