from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (
        By.XPATH,
        "//p[text()='Конструктор']"
    )

    # Кнопка "Лента заказов"
    ORDER_FEED_BUTTON = (
        By.XPATH,
        "//p[text()='Лента Заказов']"
    )


class IngredientLocators:
    # Флюоресцентная булка R2-D3
    BUN = (
        By.XPATH,
        "//*[text()='Флюоресцентная булка R2-D3']"
    )

    # Заголовок модального окна
    INGREDIENT_DETAILS = (
        By.XPATH,
        "//*[text()='Детали ингредиента']"
    )

    # Кнопка закрытия модального окна
    CLOSE_MODAL_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__')]//button"
    )

    # Счётчик булки
    BUN_COUNTER = (
        By.XPATH,
        "//*[text()='Флюоресцентная булка R2-D3']"
        "/ancestor::a[1]//p[contains(@class, 'counter_counter__num')]"
    )

    # Область конструктора бургера
    BURGER_CONSTRUCTOR = (
        By.XPATH,
        "//section[contains(@class, 'burger-constructor_burgerConstructor')]"
    )


class OrderFeedLocators:
    # Заголовок ленты заказов
    ORDER_FEED_TITLE = (
        By.XPATH,
        "//*[text()='Лента заказов']"
    )

    # Счётчик выполненных заказов за всё время
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        "//*[text()='Выполнено за все время:']"
        "/following-sibling::*[1]"
    )

    # Счётчик выполненных заказов за сегодня
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        "//*[text()='Выполнено за сегодня:']"
        "/following-sibling::*[1]"
    )

    # Раздел заказов в работе
    ORDERS_IN_PROGRESS = (
        By.XPATH,
        "//*[text()='В работе:']"
        "/following-sibling::*[1]"
    )

    # Номера заказов в ленте
    ORDER_NUMBERS = (
        By.XPATH,
        "//p[contains(@class, 'text_type_digits-default')]"
    )


class OrderPageLocators:
    # Булка для оформления заказа
    BUN = (
        By.XPATH,
        "//*[text()='Флюоресцентная булка R2-D3']"
    )

    # Соус для оформления заказа
    FILLING = (
        By.XPATH,
        "//*[text()='Соус Spicy-X']"
    )

    # Область конструктора
    CONSTRUCTOR = (
        By.XPATH,
        "//section[contains(@class, 'burger-constructor')]"
    )

    # Кнопка оформления заказа
    ORDER_BUTTON = (
        By.XPATH,
        "//button[contains(text(), 'Оформить заказ')]"
    )

    # Номер оформленного заказа
    ORDER_NUMBER = (
        By.XPATH,
        "//h2[contains(@class, 'text_type_digits-large')]"
    )

    # Кнопка закрытия окна заказа
    CLOSE_ORDER_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal__')]//button"
    )