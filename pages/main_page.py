from pages.base_page import BasePage
from locators import MainLocators
import allure

class MainPage(BasePage):
    @allure.step("Перейти в Ленту заказов")
    def go_to_feed(self): self.click(MainLocators.ORDER_FEED_LINK)

    @allure.step("Перейти в Конструктор")
    def go_to_constructor(self): self.click(MainLocators.CONSTRUCTOR_LINK)

    @allure.step("Добавить ингредиент в корзину")
    def add_ingredient(self): self.drag_and_drop(MainLocators.INGREDIENT, MainLocators.BASKET)