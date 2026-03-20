import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=20):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def find_elements(self, locator, time=20):
        WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    @allure.step("Кликнуть по элементу")
    def click(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ввести текст")
    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step("Получить текст элемента")
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step("Получить атрибут '{attr}' элемента")
    def get_attribute(self, locator, attr):
        return self.find_element(locator).get_attribute(attr)

    @allure.step("Ожидать исчезновения элемента")
    def wait_until_invisible(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.invisibility_of_element_located(locator))

    @allure.step("Ожидать увеличения значения счетчика")
    def wait_for_value_increase(self, locator, old_value, time=30):
        return WebDriverWait(self.driver, time).until(
            lambda d: int(d.find_element(*locator).text) > int(old_value)
        )
            
    def drag_and_drop(self, source_locator, target_locator):
        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)

        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)