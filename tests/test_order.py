import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData, Urls


@allure.suite('Заказ самоката')
class TestOrder:

    @allure.title('Позитивный сценарий заказа через кнопку «Заказать» вверху страницы')
    @allure.description('Переходим в форму заказа по верхней кнопке, заполняем оба шага формы, '
                        'подтверждаем заказ и проверяем, что появилось окно «Заказ оформлен»')
    def test_order_from_top_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.close_cookie_banner()

        main_page.click_order_button_top()
        order_page.make_order(OrderData.FIRST_ORDER)

        assert order_page.is_order_success_displayed()
        assert 'Заказ оформлен' in order_page.get_order_success_text()

    @allure.title('Позитивный сценарий заказа через кнопку «Заказать» внизу страницы')
    @allure.description('Переходим в форму заказа по нижней кнопке, заполняем оба шага формы, '
                        'подтверждаем заказ и проверяем, что появилось окно «Заказ оформлен»')
    def test_order_from_bottom_button(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.close_cookie_banner()

        main_page.click_order_button_bottom()
        order_page.make_order(OrderData.SECOND_ORDER)

        assert order_page.is_order_success_displayed()
        assert 'Заказ оформлен' in order_page.get_order_success_text()


@allure.suite('Логотипы в шапке')
class TestLogos:

    @allure.title('Клик по логотипу «Самоката» ведёт на главную страницу')
    @allure.description('Со страницы заказа кликаем по логотипу «Самоката» и проверяем, '
                        'что открылась главная страница с разделом «Вопросы о важном»')
    def test_scooter_logo_leads_to_main_page(self, driver):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        main_page.click_order_button_top()

        main_page.click_scooter_logo()

        assert main_page.is_main_page_opened()
        assert main_page.get_current_url() == Urls.BASE_URL

    @allure.title('Клик по логотипу Яндекса открывает Дзен в новой вкладке')
    @allure.description('Кликаем по логотипу Яндекса, переключаемся на новую вкладку '
                        'и проверяем, что через редирект открылась главная страница Дзена')
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        main_page = MainPage(driver)
        main_page.close_cookie_banner()
        windows_before = driver.window_handles

        main_page.click_yandex_logo()

        main_page.wait_for_new_window(len(windows_before))
        main_page.switch_to_new_window(windows_before)

        assert main_page.wait_for_url_contains(Urls.DZEN_URL)
