import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    """Страница оформления заказа самоката (два шага формы и всплывающие окна)."""

    # --- Первый шаг: «Для кого самокат» ---

    @allure.step('Проверяем, что открылся первый шаг формы заказа')
    def is_first_step_opened(self):
        return self.is_displayed(OrderPageLocators.FIRST_STEP_TITLE)

    @allure.step('Вводим имя: {name}')
    def fill_name(self, name):
        self.fill_input(OrderPageLocators.NAME_INPUT, name)

    @allure.step('Вводим фамилию: {surname}')
    def fill_surname(self, surname):
        self.fill_input(OrderPageLocators.SURNAME_INPUT, surname)

    @allure.step('Вводим адрес: {address}')
    def fill_address(self, address):
        self.fill_input(OrderPageLocators.ADDRESS_INPUT, address)

    @allure.step('Выбираем станцию метро: {station}')
    def select_metro_station(self, station):
        # Вводим название в поле поиска и кликаем по подходящему варианту
        self.fill_input(OrderPageLocators.METRO_INPUT, station)
        option_locator = self.format_locator(OrderPageLocators.METRO_OPTION_TEMPLATE, station)
        self.click(option_locator)

    @allure.step('Вводим телефон: {phone}')
    def fill_phone(self, phone):
        self.fill_input(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Кликаем по кнопке «Далее»')
    def click_next_button(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполняем первый шаг формы «Для кого самокат»')
    def fill_first_step(self, name, surname, address, station, phone):
        self.fill_name(name)
        self.fill_surname(surname)
        self.fill_address(address)
        self.select_metro_station(station)
        self.fill_phone(phone)
        self.click_next_button()

    # --- Второй шаг: «Про аренду» ---

    @allure.step('Проверяем, что открылся второй шаг формы заказа')
    def is_second_step_opened(self):
        return self.is_displayed(OrderPageLocators.SECOND_STEP_TITLE)

    @allure.step('Вводим дату доставки: {date}')
    def fill_delivery_date(self, date):
        # Вводим дату с клавиатуры и нажимаем Enter, чтобы закрыть календарь
        date_input = self.wait_for_visibility(OrderPageLocators.DATE_INPUT)
        date_input.send_keys(date)
        date_input.send_keys(Keys.ENTER)

    @allure.step('Выбираем срок аренды: {period}')
    def select_rent_period(self, period):
        self.click(OrderPageLocators.RENT_PERIOD_DROPDOWN)
        option_locator = self.format_locator(OrderPageLocators.RENT_PERIOD_OPTION_TEMPLATE, period)
        self.click(option_locator)

    @allure.step('Выбираем цвет самоката: {color}')
    def select_color(self, color):
        # color принимает значение 'black' или 'grey'
        if color == 'black':
            self.click(OrderPageLocators.COLOR_BLACK_CHECKBOX)
        elif color == 'grey':
            self.click(OrderPageLocators.COLOR_GREY_CHECKBOX)

    @allure.step('Вводим комментарий для курьера: {comment}')
    def fill_comment(self, comment):
        if comment:
            self.fill_input(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step('Кликаем по кнопке «Заказать» в форме')
    def click_order_button(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Заполняем второй шаг формы «Про аренду»')
    def fill_second_step(self, date, period, color, comment):
        self.fill_delivery_date(date)
        self.select_rent_period(period)
        self.select_color(color)
        self.fill_comment(comment)
        self.click_order_button()

    # --- Всплывающие окна ---

    @allure.step('Подтверждаем заказ кнопкой «Да»')
    def confirm_order(self):
        self.click(OrderPageLocators.CONFIRM_YES_BUTTON)

    @allure.step('Проверяем, что появилось окно «Заказ оформлен»')
    def is_order_success_displayed(self):
        return self.is_displayed(OrderPageLocators.ORDER_SUCCESS_TITLE)

    @allure.step('Получаем текст заголовка окна успешного заказа')
    def get_order_success_text(self):
        return self.get_text(OrderPageLocators.ORDER_SUCCESS_TITLE)

    # --- Шаг целиком ---

    @allure.step('Оформляем заказ полностью: оба шага формы и подтверждение')
    def make_order(self, order_data):
        self.fill_first_step(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['station'],
            order_data['phone']
        )
        self.fill_second_step(
            order_data['date'],
            order_data['period'],
            order_data['color'],
            order_data['comment']
        )
        self.confirm_order()
