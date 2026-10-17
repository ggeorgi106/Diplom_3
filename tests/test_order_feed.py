import allure

from pages.order_page import OrderPage
from pages.order_feed_page import OrderFeedPage


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("После оформления заказа увеличивается счётчик за всё время")
    def test_total_orders_counter_increases(self, driver):
        order_feed = OrderFeedPage(driver)
        order_page = OrderPage(driver)

        order_feed.open_order_feed()
        total_before = order_feed.get_total_orders()

        order_page.create_order()

        order_feed.open_order_feed()
        order_feed.wait_total_orders_increase(total_before)

        total_after = order_feed.get_total_orders()

        assert total_after > total_before

    @allure.title("После оформления заказа увеличивается счётчик за сегодня")
    def test_today_orders_counter_increases(self, driver):
        order_feed = OrderFeedPage(driver)
        order_page = OrderPage(driver)

        order_feed.open_order_feed()
        today_before = order_feed.get_today_orders()

        order_page.create_order()

        order_feed.open_order_feed()
        order_feed.wait_today_orders_increase(today_before)

        today_after = order_feed.get_today_orders()

        assert today_after > today_before

    @allure.title("Номер нового заказа появляется в разделе В работе")
    def test_new_order_appears_in_progress(self, driver):
        order_feed = OrderFeedPage(driver)
        order_page = OrderPage(driver)

        order_number = order_page.create_order()

        order_feed.open_order_feed()

        assert order_feed.is_order_in_progress(order_number)