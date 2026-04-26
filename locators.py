from selenium.webdriver.common.by import By

class AuthLocators:
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input")
    PASS_FIELD = (By.XPATH, ".//input[@type='password']")
    LOGIN_BTN = (By.XPATH, ".//button[text()='Войти']")

class MainLocators:
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']/parent::a")
    ORDER_FEED_LINK = (By.XPATH, ".//p[text()='Лента Заказов']/parent::a")
    INGREDIENT = (By.XPATH, "(//a[contains(@class, 'BurgerIngredient_ingredient')])[1]")
    BASKET = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    ORDER_BTN = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_ID = (By.XPATH, ".//h2[contains(@class, 'id') and not(text()='999999')]")
    MODAL = (By.XPATH, ".//*[contains(@class, 'Modal_modal_opened')]")
    CLOSE_MODAL = (By.XPATH, ".//button[contains(@class, 'close')] | .//*[contains(@class, 'Modal_modal__close')]")
    COUNTER = (By.XPATH, ".//*[contains(@class, 'counter_counter__num')]")

class FeedLocators:
    TOTAL = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    TODAY = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    IN_WORK = (By.XPATH, ".//*[contains(@class, 'orderListReady')]//li")