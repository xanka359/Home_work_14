import allure

from neoflex.pages.neoflex_contacts import neoflex_contact_details


def test_search_contacts_in_city():

    with allure.step("Открыть главную страницу сайта Neoflex"):
        neoflex_contact_details.open()

    with allure.step("Выбрать контактный город из списка"):
        neoflex_contact_details.search_contacts_in_city()

    with allure.step("Проверить контактный адрес выбранного гоорода"):
        neoflex_contact_details.address_should_contain()