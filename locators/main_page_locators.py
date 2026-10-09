from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка «да все привыкли» в плашке про куки
    COOKIE_BUTTON = (By.CLASS_NAME, 'App_CookieButton__3cvqF')

    # Кнопка «Заказать» вверху страницы (в шапке)
    ORDER_BUTTON_TOP = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    # Кнопка «Заказать» внизу страницы (большая, в конце главной)
    ORDER_BUTTON_BOTTOM = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    # Логотип «Самоката» в шапке
    SCOOTER_LOGO = (By.CLASS_NAME, 'Header_LogoScooter__3lsAR')
    # Логотип Яндекса в шапке
    YANDEX_LOGO = (By.CLASS_NAME, 'Header_LogoYandex__3TSOI')

    # Заголовок раздела «Вопросы о важном»
    FAQ_TITLE = (By.XPATH, "//div[contains(@class, 'Home_SubHeader') and text()='Вопросы о важном']")

    # Шаблоны локаторов для вопросов и ответов в разделе «Вопросы о важном».
    # Вместо {} подставляется индекс вопроса от 0 до 7.
    FAQ_QUESTION_TEMPLATE = (By.ID, 'accordion__heading-{}')
    FAQ_ANSWER_TEMPLATE = (By.ID, 'accordion__panel-{}')
