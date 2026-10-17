import allure

from pages.main_page import MainPage


@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход в раздел Лента заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_order_feed()

        assert main_page.is_order_feed_opened()

    @allure.title("Переход в раздел Конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_order_feed()
        main_page.is_order_feed_opened()
        main_page.click_constructor()

        assert main_page.is_constructor_opened()