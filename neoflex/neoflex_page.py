import time

from selene import have, by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium.webdriver import ActionChains


class NeoflexPage:

    def open(self):
        browser.open('https://www.neoflex.ru/')
        return self

    def select_solutions_form(self):
        s('.navbar__link').should(have.text('Решения')).hover()
        return self

    def check_contains_OpenAI(self):
        self.select_solutions_form()
        s('[href="/solutions/open-api"]').click()
        ActionChains(browser.driver).move_by_offset(-50, 0).perform()  #сдвигаем позицию указателя влево
        s('.service__head').should(have.text('OpenAPI'))
        return self

    def select_cases_form(self):
        s('[href="/project-list"]').should(have.text('Кейсы')).click()
        return self

    def select_expertises_form(self):
        s('[href="/expertises"]').should(have.text('Экспертиза')).hover()
        return self

    def check_contains_microservices(self):
        self.select_expertises_form()
        s('[href="/expertises/microservices"]').click() #.
        time.sleep(2)
        ActionChains(browser.driver).move_by_offset(-500, 0).perform()  #сдвигаем позицию указателя влево
        s('[href="/expertises/fast-data"]').element(by.text('Микросервисы'))
        return self

    def select_company_info_form(self):
        s('[href="/about/company"]').should(have.text('О компании')).hover()
        return self

    def check_company_history(self):
        self.select_company_info_form()
        s('[href="/about/history"]').click()
        s('.history').should(have.text('История компании'))
        return self

    def select_career_form(self):
        s('[href="/about/career"]').should(have.text('Карьера')).click()
        return self


    def type_vacancy_tester(self):
        s('#career-vacancy').should(be.visible)
        s('#input-147').set_value('тестировщик')
        time.sleep(3)
        s('.career-vacancy-form').element('[type="button"]').should(have.text('Подобрать')).click()
        time.sleep(1)
        return self

    def search_appropriate_vacancy(self):
        s('.career-vacancy-name').should(have.text('тестировщик'))
        s('.career-vacancy-location').should(have.text('Саратов'))


        #    def type_vacancy_qe_engineer(self):
        #        s('#input-147').type('qa engineer')
        #        s('.career-vacancy-form').element(by.text('Подобрать').click)
        #        return self

    def select_press_center_form(self):
        s('[href="/press-center"]').should(have.text('Пресс-центр')).click()
        return self

    def select_contacts_form(self):
        s('[href="/contacts"]').should(have.text('Контакты')).click()
        return self

    def search_for_vacancy(self):
        s('.navbar__right').element('.search').click()
        s('.search-modal__wrap').element('[placeholder="Поиск"]').click().type('вакансии')
        s('.search-count--fb').should(have.text('Найдено:'))

    def clik_on_connection_button(self):
        s('.base-button footer__button').should(have.text('Связаться с нами')).click()
        s('.feedback-modal__close').click()

    def solutions(self):
        self.check_contains_OpenAI()
        return self

    def cases(self):
        self.select_cases_form()
        #s('.base-container').should(have.exact_text('Кейсы'))
        return self

    def expertise(self):
        self.check_contains_microservices()
        return self

    def company_history(self):
        self.check_company_history()
        return self

    def career(self):
        self.select_career_form()
        s('#career-vacancy').should(have.text('Работа в Neoflex'))
        return self

    def vacancy_in_career(self):
        self.select_career_form()
        time.sleep(1)
        self.type_vacancy_tester()
        time.sleep(3)
        self.search_appropriate_vacancy()
        return self

    def press_center(self):
        self.select_press_center_form()
        s('.PressCenter').should(have.text('Пресс-центр'))
        return self

    def contacts(self):
        self.select_contacts_form()
        s(by.text(('Наши контакты')))
        return self

    def search_possibility(self):
        self.search_for_vacancy()
        return self

    def connection_button(self):
        self.clik_on_connection_button()
        return self
