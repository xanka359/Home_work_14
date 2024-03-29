import time
from asyncio import wait_for

from selene import browser, have, be
from selene.support.shared.jquery_style import s
from selenium.webdriver.support import wait


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

    def type_vacancy_tester(self):
        s('#career-vacancy').should(be.visible)
        s('#input-147').with_(timeout=3).set_value('тестировщик')
        # time.sleep(3)
        s('.career-vacancy-form').element('[type="button"]').with_(timeout=1).should(have.text('Подобрать')).click()
        # time.sleep(1)
        return self

    def search_appropriate_vacancy(self):
        s('.career-vacancy-name').should(have.text('тестировщик'))
        s('.career-vacancy-location').should(have.text('Саратов'))

    def vacancy_in_career(self):
        self.select_career_form()
        browser.config.timeout = 1
        #time.sleep(2)
        self.type_vacancy_tester()
        browser.config.timeout = 3  #time.sleep(3)
        return self


        #    def type_vacancy_qe_engineer(self):
        #        s('#input-147').type('qa engineer')
        #        s('.career-vacancy-form').element(by.text('Подобрать').click)
        #        return self

neoflex_career = NeoflexCareer()