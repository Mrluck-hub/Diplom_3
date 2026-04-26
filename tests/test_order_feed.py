import allure
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.base_page import BasePage
from locators import FeedLocators
from data import TestData
from locators import MainLocators

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Увеличение счетчика 'Выполнено за всё время'")
    def test_total_counter_increases(self, driver):
        login_p, main_p, feed_p, base_p = LoginPage(driver), MainPage(driver), FeedPage(driver), BasePage(driver)
        login_p.login(TestData.USER_EMAIL, TestData.USER_PASS)
        
        main_p.go_to_feed()
        old_total = feed_p.get_total_count()
        
        main_p.go_to_constructor()
        main_p.create_order_and_get_id()
        base_p.find_element(MainLocators.CLOSE_MODAL)
        main_p.click(MainLocators.CLOSE_MODAL)
        main_p.go_to_feed()
        assert feed_p.wait_for_value_increase(FeedLocators.TOTAL, old_total)

    @allure.title("Увеличение счетчика 'Выполнено за сегодня'")
    def test_today_counter_increases(self, driver):
        login_p, main_p, feed_p = LoginPage(driver), MainPage(driver), FeedPage(driver)
        login_p.login(TestData.USER_EMAIL, TestData.USER_PASS)
        
        main_p.go_to_feed()
        old_today = feed_p.get_today_count()
        
        main_p.go_to_constructor()
        main_p.create_order_and_get_id()
        main_p.click(MainLocators.CLOSE_MODAL)
        main_p.go_to_feed()


        assert feed_p.wait_for_value_increase(FeedLocators.TODAY, old_today)

    @allure.title("Заказ в разделе 'В работе'")
    def test_order_appears_in_work_list(self, driver):
        login_p, main_p, feed_p, base_p = LoginPage(driver), MainPage(driver), FeedPage(driver), BasePage(driver)
        login_p.login(TestData.USER_EMAIL, TestData.USER_PASS)
        
        main_p.go_to_constructor()
        order_id = main_p.create_order_and_get_id()
        base_p.find_element(MainLocators.CLOSE_MODAL)
        main_p.click(MainLocators.CLOSE_MODAL)
        main_p.go_to_feed()


        assert feed_p.is_order_in_work_list(order_id)