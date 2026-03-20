from pages.base_page import BasePage
from locators import MainLocators
import allure

class MainPage(BasePage):
    @allure.step("Перейти в Ленту заказов")
    def go_to_feed(self): self.click(MainLocators.ORDER_FEED_LINK)

    @allure.step("Перейти в Конструктор")
    def go_to_constructor(self): self.click(MainLocators.CONSTRUCTOR_LINK)

    @allure.step("Добавить ингредиент в корзину")
    def add_ingredient_to_basket(self): 
        self.drag_and_drop(MainLocators.INGREDIENT, MainLocators.BASKET)

    @allure.step("Оформить заказ и получить ID")
    def create_order_and_get_id(self):
        self.drag_and_drop(MainLocators.INGREDIENT, MainLocators.BASKET)
        self.click(MainLocators.ORDER_BTN)
        order_id = self.get_text(MainLocators.ORDER_ID).replace("#", "").strip()
        self.click(MainLocators.CLOSE_MODAL)
        self.wait_until_invisible(MainLocators.MODAL)
        return order_id