from selene import browser, have, by
from selene.support.shared.jquery_style import s


class MainMenuContacts:

    def open(self):
        browser.open('/')
        return self

    def select_contacts_form(self):
        s('[href="/contacts"]').should(have.text('Контакты')).click()
        return self

    def check_page_contacts(self):
        s(by.text(('Наши контакты')))
        return self

    def select_city(self):
        s('.contacts-cities-container').element(by.text('Саратов')).click()
        return self

    def address_should_contain(self):
        s('.address-block').should(have.text('410012, г. Саратов'))
        return self

    def search_contacts_in_city(self):
        self.select_contacts_form()
        self.check_page_contacts()
        self.select_city()


neoflex_contact_details = MainMenuContacts()
