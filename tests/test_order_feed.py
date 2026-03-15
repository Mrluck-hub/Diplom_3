import pytest
import time
import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.feed_page import FeedPage
from locators import MainLocators, FeedLocators
from selenium.webdriver.support.wait import WebDriverWait

@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Проверка счетчиков и заказов 'В работе'")
    def test_order_flow_and_counters(self, driver, user_creds):
        LoginPage(driver).login(user_creds['email'], user_creds['pass'])
        main, feed = MainPage(driver), FeedPage(driver)

        main.go_to_feed()
        WebDriverWait(driver, 15).until(lambda d: d.find_element(*FeedLocators.TOTAL).text.isdigit())
        old_total = int(feed.get_total())
        old_today = int(feed.get_today())

        main.go_to_constructor()
        main.add_ingredient()
        main.click(MainLocators.ORDER_BTN)
        
        WebDriverWait(driver, 35).until(lambda d: d.find_element(*MainLocators.ORDER_ID).text != "999999")
        order_num = main.find_element_with_wait(MainLocators.ORDER_ID).text.replace("#", "").strip()
        main.click(MainLocators.CLOSE_MODAL)

        main.go_to_feed()
        for _ in range(15):
            if int(feed.get_total()) > old_total: break
            time.sleep(1)

        assert int(feed.get_total()) > old_total
        assert int(feed.get_today()) > old_today
        assert any(order_num in val for val in feed.get_in_work_orders())