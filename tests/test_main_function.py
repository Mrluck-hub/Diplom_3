import pytest
import allure
from pages.main_page import MainPage
from locators import MainLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Основная функциональность")
class TestMainFunction:
    @allure.title("Переход в Конструктор")
    def test_constructor_transition(self, driver):
        page = MainPage(driver)
        page.go_to_feed()
        page.go_to_constructor()
        header_link = page.find_element_with_wait(MainLocators.CONSTRUCTOR_LINK)
        assert "active" in header_link.get_attribute("class")

    @allure.title("Модальное окно ингредиента")
    def test_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.click(MainLocators.INGREDIENT)
        assert page.find_element_with_wait(MainLocators.MODAL).is_displayed()
        page.click(MainLocators.CLOSE_MODAL)
        assert WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(MainLocators.MODAL))

    @allure.title("Счетчик ингредиента")
    def test_counter_increment(self, driver):
        page = MainPage(driver)
        page.add_ingredient()
        assert int(page.find_element_with_wait(MainLocators.COUNTER).text) > 0