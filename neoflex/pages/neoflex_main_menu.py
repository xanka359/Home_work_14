from selene import have, by
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


class NeoflexMainMenu:

    def open(self):
        browser.open('/')
        return self

    class MainMenuSolution:
        def select_solutions_form(self):
            s('.navbar__link').should(have.text('Решения')).hover()
            return self

        def open_point_OpenAI(self):
            self.select_solutions_form()
            s('[href="/solutions/open-api"]').click()
            browser.driver.execute_script('window.scrollBy(-50, 0);')

        def check_contains_OpenAI(self):
            s('.service__head').should(have.text('OpenAPI'))
            return self

        def main_menu_solution(self):
            self.select_solutions_form()
            self.open_point_OpenAI()
            self.check_contains_OpenAI()

    class MainMenuCases:
        def select_cases_form(self):
            s('[href="/project-list"]').should(have.text('Кейсы')).click()
            return self

        def check_cases_form(self):
            s('.base-container').element(by.text('Кейсы'))

        def main_menu_cases(self):
            self.select_cases_form()
            self.check_cases_form()

    class MainMenuExpertises:
        def select_expertises_form(self):
            s('[href="/expertises"]').should(have.text('Экспертиза')).hover()
            return self

        def open_point_microservices(self):
            self.select_expertises_form()
            s('[href="/expertises/microservices"]').click()
            browser.driver.execute_script('window.scrollBy(-500, 0);')

        def check_contains_microservices(self):
            s('[href="/expertises/fast-data"]').with_(timeout=4).element(by.text('Микросервисы'))
            return self

        def main_menu_expertises(self):
            self.select_expertises_form()
            self.open_point_microservices()
            self.check_contains_microservices()

    class MainMenuCompanyInfo:

        def select_company_info_form(self):
            s('[href="/about/company"]').should(have.text('О компании')).hover()
            return self

        def open_point_history(self):
            self.select_company_info_form()
            s('[href="/about/history"]').click()
            return self

        def check_company_history(self):
            s('.history').should(have.text('История компании'))
            return self

        def main_menu_companyInfo(self):
            self.select_company_info_form()
            self.open_point_history()
            self.check_company_history()

    class MainMenuPressCenter:

        def select_press_center_form(self):
            s('[href="/press-center"]').should(have.text('Пресс-центр')).click()
            return self

        def check_page_press_center(self):
            s('.PressCenter').should(have.text('Пресс-центр'))
            return self

        def main_menu_press_center(self):
            self.select_press_center_form()
            self.check_page_press_center()

    def open_points_mein_menu(self):
        neoflex_page = NeoflexMainMenu()
        neoflex_page.MainMenuSolution().main_menu_solution()
        neoflex_page.MainMenuCases().main_menu_cases()
        neoflex_page.MainMenuExpertises().main_menu_expertises()
        neoflex_page.MainMenuCompanyInfo().main_menu_companyInfo()
        neoflex_page.MainMenuPressCenter().main_menu_press_center()

    def check_main_menu_points(self):
        menu_items = s('.navbar__list').all('li.navbar__item')
        menu_texts = ['Решения', 'Кейсы', 'Экспертиза', 'О компании', 'Карьера', 'Пресс-центр', 'Контакты']
        menu_items.should(have.exact_texts(*menu_texts))
        return self


neoflex_page = NeoflexMainMenu()
