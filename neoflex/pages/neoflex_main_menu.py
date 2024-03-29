from selene.api import browser
from selene import have, by, be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s
from selenium.webdriver import ActionChains


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
            #ActionChains(browser.driver).move_by_offset(-50, 0).perform()  #сдвигаем позицию указателя влево
            browser.driver.execute_script('window.scrollBy(-50, 0);')

        def check_contains_OpenAI(self):
            s('.service__head').should(have.text('OpenAPI'))
            return self

    class MainMenuCases:
        def select_cases_form(self):
            s('[href="/project-list"]').should(have.text('Кейсы')).click()
            return self

        def check_cases_form(self):
            s('.base-container').element(by.text('Кейсы'))

    class MainMenuExpertises:
        def select_expertises_form(self):
            s('[href="/expertises"]').should(have.text('Экспертиза')).hover()
            return self

        def open_point_microservices(self):
            self.select_expertises_form()
            s('[href="/expertises/microservices"]').click()
            #time.sleep(2)
            #ActionChains(browser.driver).move_by_offset(-500, 0).perform()  #сдвигаем позицию указателя влево
            browser.driver.execute_script('window.scrollBy(-500, 0);')

        def check_contains_microservices(self):
            s('[href="/expertises/fast-data"]').with_(timeout=4).element(by.text('Микросервисы'))
            return self

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

    class MainMenuPressCenter:

        def select_press_center_form(self):
            s('[href="/press-center"]').should(have.text('Пресс-центр')).click()
            return self

        def check_page_press_center(self):
            s('.PressCenter').should(have.text('Пресс-центр'))
            return self

    class MainMenuContacts:
        def select_contacts_form(self):
            s('[href="/contacts"]').should(have.text('Контакты')).click()
            return self

        def check_page_contacts(self):
            s(by.text(('Наши контакты')))
            return self


neoflex_page = NeoflexMainMenu()