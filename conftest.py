import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: type1 or type2"
    )

@pytest.fixture(scope="class")
def setup(request):

    browser_named = request.config.getoption("browser")

    if browser_named == "chrome":
        driver = webdriver.Chrome()
    elif browser_named == "safari":
        driver = webdriver.Safari()
    driver.get("https://pl-upgrade-customizer-stg.qstrike.net/")
    request.cls.driver = driver
    driver.maximize_window()
    yield
    time.sleep(3)
    driver.quit()
    
@pytest.fixture()
def URL(request):
    url_name = "https://pl-upgrade-customizer-stg.qstrike.net/"
    request.cls.url_name = url_name

# Prequesites for accessing the pl upgrade page
    
