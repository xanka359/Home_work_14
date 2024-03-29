from selene import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

class NeoflexSearch:

    def open(self):
        browser.open('/')
        return self

    def search_for_vacancy(self):
        s('.navbar__right').element('.search').click()
        s('.search-modal__wrap').element('[placeholder="Поиск"]').click().type('вакансии')

    def search_possibility(self):
        self.search_for_vacancy()
        s('.search-count--fb').should(have.text('Найдено:'))
        return self


neoflex_search = NeoflexSearch()