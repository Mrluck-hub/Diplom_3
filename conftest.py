import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get("https://stellarburgers.education-services.ru")
    yield browser
    browser.quit()

@pytest.fixture
def user_creds():
    return {"email": "Melnikov_38@gmail.com", "pass": "olegoleg1"}