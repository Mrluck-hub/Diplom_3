import allure
from pages.main_page import MainPage
from locators import MainLocators

@allure.feature("Основная функциональность")
class TestMainFunction:
    @allure.title("Переход в Конструктор")
    def test_transition_to_constructor(self, driver):
        page = MainPage(driver)
        page.go_to_feed()
        page.go_to_constructor()
        assert "active" in page.get_attribute(MainLocators.CONSTRUCTOR_LINK, "class")

    @allure.title("Переход в Ленту заказов")
    def test_transition_to_feed(self, driver):
        page = MainPage(driver)
        page.go_to_feed()
        assert "active" in page.get_attribute(MainLocators.ORDER_FEED_LINK, "class")

    @allure.title("Модальное окно ингредиента")
    def test_open_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.click(MainLocators.INGREDIENT)
        assert page.find_element(MainLocators.MODAL).is_displayed()

    @allure.title("Закрытие модального окна ингредиента")
    def test_close_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.click(MainLocators.INGREDIENT)
        page.click(MainLocators.CLOSE_MODAL)
        assert page.wait_until_invisible(MainLocators.MODAL)

    @allure.title("Счетчик ингредиента")
    def test_counter_increment(self, driver):
        page = MainPage(driver)
        try:
            old_val = int(page.get_text(MainLocators.COUNTER))
        except:
            old_val = 0
        page.add_ingredient_to_basket()
        new_val = int(page.get_text(MainLocators.COUNTER))
        assert new_val > old_val