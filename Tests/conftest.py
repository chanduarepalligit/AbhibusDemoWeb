import os
from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def web_driver(request):
    URL = "http://stagingapsrtc.abhibus.com/oprs-web/"
    ChromeDriver = "C:\\Users\\Chandu\\Downloads\\chromedriver_win32\\chromedriver.exe"
    os.environ["webdriver.chrome.driver"] = ChromeDriver
    driver = webdriver.Chrome(ChromeDriver)
    driver.maximize_window()
    driver.get(URL)
    driver.implicitly_wait(2)
    request.cls.driver = driver
    yield
    driver.close()
