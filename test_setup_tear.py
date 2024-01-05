import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
@pytest.fixture(scope="function")
def setup_driver():
    option = webdriver.ChromeOptions()
    option.add_argument("--start-maximized")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])

    # initiate Chrome driver using ChromeDriverManager and options
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=option)
    driver.get('https://www.saucedemo.com/')
    print("Setup driver")
    yield
    driver.close()
    print("Teardown driver")


@pytest.mark.usefixtures("setup_driver")
def setup_onboarding(setup_driver):
    setup_driver.driver.get("")
    print("User login")
    yield
    print("User logout")


class TestExample:

    def test_addition(self, setup_driver, setup_onboarding):
        assert 1 + 1 == 2

    def test_subtraction(self, setup_driver, setup_onboarding):
        assert 3 - 1 == 2
