from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from urls import BASE_URL
from locators import MainPageLocators, IngredientLocators


class MainPage(BasePage):

    def open_main_page(self):
        self.open_page(BASE_URL)

    def click_constructor(self):
        self.click_element(
            MainPageLocators.CONSTRUCTOR_BUTTON
        )

    def click_order_feed(self):
        self.click_element(
            MainPageLocators.ORDER_FEED_BUTTON
        )

    def is_order_feed_opened(self):
        return self.wait.until(
            EC.url_contains("/feed")
        )

    def is_constructor_opened(self):
        return self.wait.until(
            lambda driver: driver.current_url.rstrip("/")
            == BASE_URL.rstrip("/")
        )

    def click_ingredient(self):
        self.click_element(
            IngredientLocators.BUN
        )

    def is_ingredient_modal_open(self):
        return self.find_element(
            IngredientLocators.INGREDIENT_DETAILS
        ).is_displayed()

    def close_ingredient_modal(self):
        self.click_element(
            IngredientLocators.CLOSE_MODAL_BUTTON
        )

    def is_ingredient_modal_closed(self):
        return self.wait.until(
            EC.invisibility_of_element_located(
                IngredientLocators.INGREDIENT_DETAILS
            )
        )

    def get_bun_counter(self):
        elements = self.driver.find_elements(
            *IngredientLocators.BUN_COUNTER
        )

        if not elements:
            return 0

        return int(elements[0].text)

    def drag_bun_to_constructor(self):
        bun = self.find_element(
            IngredientLocators.BUN
        )

        constructor = self.find_element(
            IngredientLocators.BURGER_CONSTRUCTOR
        )

        ActionChains(self.driver).drag_and_drop(
            bun, constructor
        ).perform()

    def wait_for_bun_counter_increase(self, counter_before):
        return self.wait.until(
            lambda _: (
                counter_after
                if (counter_after := self.get_bun_counter())
                > counter_before
                else False
            )
        )