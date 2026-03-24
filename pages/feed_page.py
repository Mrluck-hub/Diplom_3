from pages.base_page import BasePage
from locators import FeedLocators
import allure

class FeedPage(BasePage):
    @allure.step("Получить общее количество заказов")
    def get_total_count(self):
        self.wait_for_text_to_be_digit(FeedLocators.TOTAL)
        return self.get_text(FeedLocators.TOTAL)

    @allure.step("Получить количество заказов за сегодня")
    def get_today_count(self):
        self.wait_for_text_to_be_digit(FeedLocators.TODAY)
        return self.get_text(FeedLocators.TODAY)
    
    @allure.step("Проверить наличие заказа в списке 'В работе'")
    def is_order_in_work_list(self, order_num):
        elements = self.find_elements(FeedLocators.IN_WORK)
        return any(str(order_num) in el.text for el in elements)