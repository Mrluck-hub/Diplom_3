from pages.base_page import BasePage
from locators import FeedLocators
import allure

class FeedPage(BasePage):
    @allure.step("Получить общее количество заказов")
    def get_total(self): return self.find_element_with_wait(FeedLocators.TOTAL).text
    
    @allure.step("Получить количество заказов за сегодня")
    def get_today(self): return self.find_element_with_wait(FeedLocators.TODAY).text

    @allure.step("Получить номера заказов в работе")
    def get_in_work_orders(self):
        elements = self.driver.find_elements(*FeedLocators.IN_WORK)
        return [el.text for el in elements]