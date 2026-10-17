import allure

from pages.base_page import BasePage
from locators import MainPageLocators, OrderFeedLocators
from urls import BASE_URL


class OrderFeedPage(BasePage):

    @allure.step("Открыть ленту заказов")
    def open_order_feed(self):
        self.open_page(BASE_URL)
        self.click_element(
            MainPageLocators.ORDER_FEED_BUTTON
        )

    @allure.step("Получить количество заказов за всё время")
    def get_total_orders(self):
        text = self.get_text(
            OrderFeedLocators.TOTAL_ORDERS_COUNTER
        )
        return int("".join(text.split()))

    @allure.step("Получить количество заказов за сегодня")
    def get_today_orders(self):
        text = self.get_text(
            OrderFeedLocators.TODAY_ORDERS_COUNTER
        )
        return int("".join(text.split()))

    @allure.step("Получить номера заказов в работе")
    def get_orders_in_progress(self):
        element = self.find_element(
            OrderFeedLocators.ORDERS_IN_PROGRESS
        )
        return element.text.split()

    @allure.step("Проверить наличие номера заказа в работе")
    def is_order_in_progress(self, order_number):
        return self.wait.until(
            lambda driver: str(order_number).lstrip("0")
            in [
                number.lstrip("0")
                for number in self.get_orders_in_progress()
            ]
        )

    @allure.step("Дождаться увеличения общего счётчика")
    def wait_total_orders_increase(self, previous_count):
        return self.wait.until(
            lambda driver: self.get_total_orders()
            > previous_count
        )

    @allure.step("Дождаться увеличения счётчика за сегодня")
    def wait_today_orders_increase(self, previous_count):
        return self.wait.until(
            lambda driver: self.get_today_orders()
            > previous_count
        )