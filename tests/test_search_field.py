import allure

from neoflex.pages.neoflex_search import neoflex_search


def test_search_field():

    with allure.step("Открыть главную страницу сайта Neoflex"):
        neoflex_search.open()

    with allure.step("Нажать на лупу на верхней панеле сайта"):
        neoflex_search.search_for_vacancy()

    with allure.step("Проверить результаты поиска"):
        neoflex_search.search_possibility()
