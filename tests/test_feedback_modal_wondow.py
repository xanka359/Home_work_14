import allure

from neoflex.pages.neoflex_connection_modal_window import neoflex_contacts


def test_feedback_modal_window():

    with allure.step("Открыть главную страницу сайта Neoflex"):
        neoflex_contacts.open()

    with allure.step("Отпркыть модальнео окно обратной связи"):
        neoflex_contacts.clik_on_connection_button()

    with allure.step("Заполнить модальное окно и закрыть его"):
        neoflex_contacts.check_connection_window()