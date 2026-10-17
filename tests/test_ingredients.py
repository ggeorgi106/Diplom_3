import allure

from pages.main_page import MainPage


@allure.feature("Ингредиенты")
class TestIngredients:

    @allure.title("Открытие модального окна ингредиента")
    def test_open_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_open()

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_ingredient()

        assert main_page.is_ingredient_modal_open()

        main_page.close_ingredient_modal()

        assert main_page.is_ingredient_modal_closed()

    @allure.title("Увеличение счётчика ингредиента")
    def test_ingredient_counter_increases(self, driver):
        main_page = MainPage(driver)
        main_page.open_main_page()

        counter_before = main_page.get_bun_counter()

        main_page.drag_bun_to_constructor()

        main_page.wait.until(
            lambda _: main_page.get_bun_counter()
            > counter_before
        )

        counter_after = main_page.get_bun_counter()

        assert counter_after > counter_before