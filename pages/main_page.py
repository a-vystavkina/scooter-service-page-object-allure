import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Главная страница «Самоката»."""

    @allure.step('Закрываем плашку про куки')
    def close_cookie_banner(self):
        self.click(MainPageLocators.COOKIE_BUTTON)

    @allure.step('Кликаем по вопросу номер {index} в разделе «Вопросы о важном»')
    def click_faq_question(self, index):
        question_locator = self.format_locator(MainPageLocators.FAQ_QUESTION_TEMPLATE, index)
        self.scroll_to_element(question_locator)
        self.click(question_locator)

    @allure.step('Получаем текст вопроса номер {index}')
    def get_faq_question_text(self, index):
        question_locator = self.format_locator(MainPageLocators.FAQ_QUESTION_TEMPLATE, index)
        return self.get_text(question_locator)

    @allure.step('Получаем текст ответа на вопрос номер {index}')
    def get_faq_answer_text(self, index):
        answer_locator = self.format_locator(MainPageLocators.FAQ_ANSWER_TEMPLATE, index)
        return self.get_text(answer_locator)

    @allure.step('Проверяем, что ответ на вопрос номер {index} отображается')
    def is_faq_answer_displayed(self, index):
        answer_locator = self.format_locator(MainPageLocators.FAQ_ANSWER_TEMPLATE, index)
        return self.is_displayed(answer_locator)

    @allure.step('Кликаем по кнопке «Заказать» вверху страницы')
    def click_order_button_top(self):
        self.click(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Кликаем по кнопке «Заказать» внизу страницы')
    def click_order_button_bottom(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.click(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Кликаем по логотипу «Самоката»')
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Кликаем по логотипу Яндекса')
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step('Проверяем, что главная страница открылась')
    def is_main_page_opened(self):
        return self.is_displayed(MainPageLocators.FAQ_TITLE)
