import allure
from selene import be
from selene.support.shared.jquery_style import s

from neoflex.pages.neoflex_career import neoflex_career
from neoflex.pages.neoflex_main_menu import  neoflex_page
from neoflex.pages.neoflex_search import neoflex_search


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
        neoflex_search.open()

    with allure.step("Нажать на лупу на верхней панеле сайта"):
        neoflex_search.search_for_vacancy()

    with allure.step("Проверить результаты поиска"):
        neoflex_search.search_possibility()

def test_appropriate_vacancy():

    with allure.step("Открыть главную страницу сайта Neoflex"):
        neoflex_career.open()

    with allure.step("Произвести поиск в разделе Карьера по направлению тестирования"):
        neoflex_career.vacancy_in_career()

    with allure.step("Проверить есть ли подходящие вакансии в результатах поиска"):
        neoflex_career.search_appropriate_vacancy()