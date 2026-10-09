import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    """Родительский класс для всех страниц. Хранит общие методы работы с элементами."""

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открываем страницу {url}')
    def open(self, url):
        self.driver.get(url)

    @allure.step('Ищем элемент {locator}')
    def find_element(self, locator):
        # Ждём, пока элемент появится в DOM, и возвращаем его
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(locator)
        )

    @allure.step('Ждём, пока элемент {locator} станет видимым')
    def wait_for_visibility(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(locator)
        )

    @allure.step('Ждём, пока элемент {locator} станет кликабельным')
    def wait_for_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator)
        )

    @allure.step('Кликаем по элементу {locator}')
    def click(self, locator):
        self.wait_for_clickable(locator).click()

    @allure.step('Прокручиваем страницу до элемента {locator}')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step('Вводим текст "{text}" в поле {locator}')
    def fill_input(self, locator, text):
        self.wait_for_visibility(locator).send_keys(text)

    @allure.step('Получаем текст элемента {locator}')
    def get_text(self, locator):
        return self.wait_for_visibility(locator).text

    @allure.step('Проверяем, что элемент {locator} отображается')
    def is_displayed(self, locator):
        return self.wait_for_visibility(locator).is_displayed()

    @allure.step('Формируем локатор из шаблона {template} со значением "{value}"')
    def format_locator(self, template, value):
        # template хранится как кортеж (способ поиска, строка с {}).
        # Подставляем значение и возвращаем готовый локатор.
        by, path = template
        return (by, path.format(value))

    @allure.step('Ждём, пока откроется новая вкладка')
    def wait_for_new_window(self, windows_before):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.number_of_windows_to_be(windows_before + 1)
        )

    @allure.step('Переключаемся на новую вкладку')
    def switch_to_new_window(self, windows_before):
        for window in self.driver.window_handles:
            if window not in windows_before:
                self.driver.switch_to.window(window)
                break

    @allure.step('Ждём, пока адрес страницы станет содержать "{url_part}"')
    def wait_for_url_contains(self, url_part):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.url_contains(url_part)
        )

    @allure.step('Получаем адрес текущей страницы')
    def get_current_url(self):
        return self.driver.current_url
