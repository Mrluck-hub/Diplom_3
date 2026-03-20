from pages.base_page import BasePage
from locators import FeedLocators
from selenium.webdriver.support.wait import WebDriverWait
import allure

class FeedPage(BasePage):
    @allure.step("Получить общее количество заказов")
    def get_total_count(self):
        WebDriverWait(self.driver, 25).until(lambda d: d.find_element(*FeedLocators.TOTAL).text.isdigit())
        return self.get_text(FeedLocators.TOTAL)

    @allure.step("Получить количество заказов за сегодня")
    def get_today_count(self):
        WebDriverWait(self.driver, 25).until(lambda d: d.find_element(*FeedLocators.TODAY).text.isdigit())
        return self.get_text(FeedLocators.TODAY)
    
    @allure.step("Получить номера заказов в работе")
    def is_order_in_work_list(self, order_num):
        elements = self.find_elements(FeedLocators.IN_WORK)
        return any(order_num in el.text for el in elements)