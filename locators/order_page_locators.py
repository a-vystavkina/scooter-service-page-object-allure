from selenium.webdriver.common.by import By


class OrderPageLocators:
    # --- Первый шаг формы: «Для кого самокат» ---

    # Заголовок первого шага
    FIRST_STEP_TITLE = (By.XPATH, "//div[contains(@class, 'Order_Header') and text()='Для кого самокат']")
    # Поле «Имя»
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    # Поле «Фамилия»
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    # Поле «Адрес: куда привезти заказ»
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    # Поле «Станция метро» (выпадающий список с поиском)
    METRO_INPUT = (By.CLASS_NAME, 'select-search__input')
    # Шаблон локатора для варианта станции метро в выпадающем списке.
    # Вместо {} подставляется название станции.
    METRO_OPTION_TEMPLATE = (By.XPATH, "//div[@class='Order_Text__2broi' and text()='{}']")
    # Поле «Телефон: на него позвонит курьер»
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    # Кнопка «Далее»
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # --- Второй шаг формы: «Про аренду» ---

    # Заголовок второго шага
    SECOND_STEP_TITLE = (By.XPATH, "//div[contains(@class, 'Order_Header') and text()='Про аренду']")
    # Поле «Когда привезти самокат» (дата)
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    # Выпадающий список «Срок аренды»
    RENT_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-control')
    # Шаблон локатора для варианта срока аренды.
    # Вместо {} подставляется текст, например «сутки» или «двое суток».
    RENT_PERIOD_OPTION_TEMPLATE = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']")
    # Чекбокс цвета «чёрный жемчуг»
    COLOR_BLACK_CHECKBOX = (By.ID, 'black')
    # Чекбокс цвета «серая безысходность»
    COLOR_GREY_CHECKBOX = (By.ID, 'grey')
    # Поле «Комментарий для курьера»
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    # Кнопка «Заказать» внизу формы второго шага
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    # --- Всплывающие окна ---

    # Кнопка «Да» в окне «Хотите оформить заказ?»
    CONFIRM_YES_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Modal')]//button[text()='Да']")
    # Заголовок окна с сообщением об успешном создании заказа
    ORDER_SUCCESS_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]")
    # Кнопка «Посмотреть статус» в окне успешного заказа
    SHOW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
