import allure

from selenium.webdriver.support.ui import WebDriverWait

from pages.main_page import MainPage
from urls import BASE_URL


@allure.feature("Навигация")
class TestNavigation:

    @allure.title("Переход в раздел Лента заказов")
    def test_go_to_order_feed(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_order_feed()

        WebDriverWait(driver, 10).until(
            lambda browser: "/feed" in browser.current_url
        )

        assert "/feed" in driver.current_url

    @allure.title("Переход в раздел Конструктор")
    def test_go_to_constructor(self, driver):
        main_page = MainPage(driver)

        main_page.open_main_page()
        main_page.click_order_feed()

        WebDriverWait(driver, 10).until(
            lambda browser: "/feed" in browser.current_url
        )

        main_page.click_constructor()

        WebDriverWait(driver, 10).until(
            lambda browser: browser.current_url.rstrip("/")
            == BASE_URL.rstrip("/")
        )

        assert driver.current_url.rstrip("/") == BASE_URL.rstrip("/")