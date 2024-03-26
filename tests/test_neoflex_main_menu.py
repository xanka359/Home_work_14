import allure

from neoflex.neoflex_page import NeoflexPage

neoflex_page = NeoflexPage()

def test_main_menu():

    with allure.step("Открыть главную страницу сайта Neoflex"):
        neoflex_page.open()

    with allure.step("Открыть раздел меню Решения, пункт OpenAPI"):
        neoflex_page.solutions()

    with allure.step("Открыть раздел меню Кейсы"):
        neoflex_page.cases()

    with allure.step("Открыть раздел меню Экспертиза"):
        neoflex_page.expertise()

    with allure.step("Открыть раздел меню О компании, пункт История"):
        neoflex_page.company_history()

    with allure.step("Открыть раздел меню Карьера"):
        neoflex_page.career()

    with allure.step("Открыть раздел меню Пресс-центр"):
        neoflex_page.press_center()

    with allure.step("Открыть раздел меню Контакты"):
        neoflex_page.contacts()

def test_search_field():

    with allure.step("Открыть главную страницу сайта Neoflex"):
        neoflex_page.open()

    with allure.step("Нажать на лупу на верхней панеле сайта"):
        neoflex_page.search_possibility()

def test_appropriate_vacancy():

    with allure.step("Открыть главную страницу сайта Neoflex"):
        neoflex_page.open()

    with allure.step("Произвести поиск в разделе Карьера по направлению тестирования"):
        neoflex_page.vacancy_in_career()