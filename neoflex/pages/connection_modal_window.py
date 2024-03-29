from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class NeoflexContactDetails:

    def open(self):
        browser.open('/')
        return self
    def clik_on_connection_button(self):
        s('.base-button footer__button').should(have.text('Связаться с нами')).click()
        s('.feedback-modal__close').click()

    def fill_contact_details(self):
        s('#feedbackFIO').type('Иванов Иван')
        s('#feedbackTel').hover().type(8965553211)
        s('#feedbackEmail').hover().type('example@gmail.com')
        s('#feedbackComment').type('Здравствуйте')

    def close_filled_form(self):
        s('.feedback-modal__close').click()


neoflex_contact_details = NeoflexContactDetails