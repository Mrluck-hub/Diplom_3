import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from urls import Urls

@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    if request.param == "chrome":
        browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    else:
        browser = webdriver.Firefox()
    browser.maximize_window()
    browser.get(Urls.BASE_URL)
    
    yield browser
    
    browser.quit()