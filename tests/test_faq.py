import allure
import pytest
from pages.main_page import MainPage
from data import FaqData


@allure.suite('Главная страница: раздел «Вопросы о важном»')
class TestFaq:

    @allure.title('Клик по вопросу раскрывает правильный ответ: вопрос {index}')
    @allure.description('Кликаем по стрелочке у вопроса в разделе «Вопросы о важном» '
                        'и проверяем, что открылся ответ с ожидаемым текстом')
    @pytest.mark.parametrize('index, question, answer', FaqData.QUESTIONS_AND_ANSWERS)
    def test_faq_question_shows_correct_answer(self, driver, index, question, answer):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()

        main_page.click_faq_question(index)

        assert main_page.is_faq_answer_displayed(index)
        assert main_page.get_faq_question_text(index) == question
        assert main_page.get_faq_answer_text(index) == answer
