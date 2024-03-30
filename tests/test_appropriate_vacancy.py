import allure

from neoflex.pages.neoflex_career import neoflex_career


def test_appropriate_vacancy():

    with (allure.step("Открыть главную страницу сайта Neoflex")):
        neoflex_career.open()

    with allure.step("Произвести поиск в разделе Карьера по направлению тестирования"):
        neoflex_career.vacancy_in_career()

    with allure.step("Проверить есть ли подходящие вакансии в результатах поиска"):
        neoflex_career.search_appropriate_vacancy()