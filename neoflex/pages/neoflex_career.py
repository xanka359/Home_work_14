from selene import browser, have, be
from selene.support.shared.jquery_style import s


class NeoflexCareer:

    def open(self):
        browser.open('/')
        return self

    def select_career_form(self):
        s('[href="/about/career"]').should(have.text('Карьера')).click()
        return self

    def check_page_career(self):
        s('#career-vacancy').should(have.text('Работа в Neoflex'))
        return self

    def type_vacancy_qa(self):
        s('#career-vacancy').should(be.visible)
        s('#input-147').with_(timeout=10).set_value('QA')
        s('.career-vacancy-form').element('[type="button"]').with_(timeout=10).should(have.text('Подобрать')).click()
        return self

    def search_appropriate_vacancy(self):
        s('.career-vacancy-name').should(have.text('QA'))
        s('.career-vacancy-location').should(have.text('Пенза'))

    def vacancy_in_career(self):
        self.select_career_form()
        browser.config.timeout = 10
        self.type_vacancy_qa()
        browser.config.timeout = 10
        return self

    def main_menu_career(self):
        self.select_career_form()
        self.check_page_career()


neoflex_career = NeoflexCareer()
