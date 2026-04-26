from pages.base_page import BasePage
from locators import AuthLocators, MainLocators
from urls import Urls
import allure

class LoginPage(BasePage):
    @allure.step("Авторизация под пользователем {email}")
    def login(self, email, password):
        self.open_url(Urls.LOGIN_URL)
        self.input_text(AuthLocators.EMAIL_FIELD, email)
        self.input_text(AuthLocators.PASS_FIELD, password)
        self.click(AuthLocators.LOGIN_BTN)
        self.find_element(MainLocators.ORDER_BTN)