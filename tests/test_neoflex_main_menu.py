import allure

from neoflex.pages.neoflex_main_menu import neoflex_page


def test_main_menu():

    '''GIVEN'''
    with allure.step("Открыть главную страницу сайта Neoflex"):
        neoflex_page.open()

    '''WHEN'''
    with allure.step("Проверить что все ожидаемые пункты присутствуют в верхнем меню"):
        neoflex_page.check_main_menu_points()

    '''THEN'''
    with allure.step("Проверить что все пункты верхнего меню сайта кликабельны"):
        neoflex_page.open_points_mein_menu()

