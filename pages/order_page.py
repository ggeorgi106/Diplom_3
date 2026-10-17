import allure

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators import OrderPageLocators
from urls import BASE_URL


class OrderPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open_main_page(self):
        self.open_page(BASE_URL)

    @allure.step("Перетащить булку в конструктор")
    def add_bun(self):
        bun = self.find_element(
            OrderPageLocators.BUN
        )
        constructor = self.find_element(
            OrderPageLocators.CONSTRUCTOR
        )

        ActionChains(self.driver).drag_and_drop(
            bun, constructor
        ).perform()

    @allure.step("Перетащить начинку в конструктор")
    def add_filling(self):
        filling = self.find_element(
            OrderPageLocators.FILLING
        )
        constructor = self.find_element(
            OrderPageLocators.CONSTRUCTOR
        )

        ActionChains(self.driver).drag_and_drop(
            filling, constructor
        ).perform()

    @allure.step("Нажать кнопку оформления заказа")
    def click_order_button(self):
        self.click_element(
            OrderPageLocators.ORDER_BUTTON
        )

    @allure.step("Получить номер оформленного заказа")
    def get_order_number(self):
        return self.wait.until(
            lambda driver: self._get_valid_order_number()
        )

    def _get_valid_order_number(self):
        element = self.driver.find_element(
            *OrderPageLocators.ORDER_NUMBER
        )

        number = element.text.strip()

        if number.isdigit() and int(number) > 0:
            return number

        return False

    @allure.step("Закрыть окно оформленного заказа")
    def close_order_modal(self):
        self.click_element(
            OrderPageLocators.CLOSE_ORDER_MODAL
        )

    @allure.step("Оформить новый заказ")
    def create_order(self):
        self.open_main_page()
        self.add_bun()
        self.add_filling()
        self.click_order_button()

        return self.get_order_number()