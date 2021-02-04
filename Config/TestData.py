class TestData:

    HOME_PAGE_URL = 'http://www.gidmenu.com'

    BREAKFASTS_PAGE_URL = HOME_PAGE_URL + '/restaurants/zavtraki/'

    ACCOUNT = {
        'email': 'john.doe@mail.com',
        'password': 'Hilton101',
        'invalid_email': 'john.doe@mail.con',
        'invalid_password': 'Hilton102'
    }

    RESTAURANTS_COLLECTION = [
        {
            'restaurant_name': 'PATRIARSHIE_PRUDY',
            'url': 'https://gidmenu.com/restaurants/patriarshie-prudy/?show_dish_rest_groups=N',
            'title': 'Патриаршие Пруды'
        },
        {
            'restaurant_name': 'MOSKVA_CITY',
            'url': 'https://gidmenu.com/restaurants/moskva-siti/?show_dish_rest_groups=N',
            'title': 'Москва сити',
        },
        {
            'restaurant_name': 'DEPO',
            'url': 'https://gidmenu.com/restaurants/depo/?show_dish_rest_groups=N',
            'title': 'Депо',
        },
        {
            'restaurant_name': 'TSENTRALNYY-RYNOK',
            'url': 'https://gidmenu.com/restaurants/tsentralnyy-rynok/?show_dish_rest_groups=N',
            'title': 'Центральный рынок',
        },
        {
            'restaurant_name': 'DANILOVSKIY-RYNOK',
            'url': 'https://gidmenu.com/restaurants/danilovskiy-rynok/?show_dish_rest_groups=N',
            'title': 'Даниловский рынок',
        },
        {
            'restaurant_name': 'GASTROFERMA-N1-NA-BAUMANSKOY',
            'url': 'https://gidmenu.com/restaurants/gastroferma-n1-na-baumanskoy/?show_dish_rest_groups=N',
            'title': '«Гастроферма N1» на Бауманской',
        },
        {
            'restaurant_name': 'GASTROMARKET-VOKRUG-SVETA-NA-NIKOLSKOY',
            'url': 'https://gidmenu.com/restaurants/gastromarket-vokrug-sveta-na-nikolskoy/?show_dish_rest_groups=N',
            'title': 'Гастромаркет «Вокруг света»',
        },
        {
            'restaurant_name': 'RYNOK-NA-MAROSEYKE',
            'url': 'https://gidmenu.com/restaurants/rynok-na-maroseyke/?show_dish_rest_groups=N',
            'title': 'Рынок на Маросейке',
        },
        {
            'restaurant_name': 'USACHEVSKIY-RYNOK',
            'url': 'https://gidmenu.com/restaurants/usachevskiy-rynok/?show_dish_rest_groups=N',
            'title': 'Усачевский рынок',
        },

    ]

    LIST_OF_RESTAURANTS_NAMES = [x['restaurant_name'] for x in RESTAURANTS_COLLECTION]

    LOGIN_ERROR_MESSAGE_TEXT = 'Неверный логин или пароль.'
