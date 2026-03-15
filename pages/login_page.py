from pages.base_page import BasePage
from locators import AuthLocators, MainLocators
import allure

class LoginPage(BasePage):
    @allure.step("Авторизация пользователем {email}")
    def login(self, email, password):
        self.driver.get("https://stellarburgers.education-services.ru")
        self.find_element_with_wait(AuthLocators.EMAIL_FIELD).send_keys(email)
        self.find_element_with_wait(AuthLocators.PASS_FIELD).send_keys(password)
        self.click(AuthLocators.LOGIN_BTN)
        self.find_element_with_wait(MainLocators.ORDER_BTN)