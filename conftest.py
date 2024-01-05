import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from utilities.take_screenshot import TakeScreenshot as TS

url = "https://www.saucedemo.com/"


@pytest.fixture
def setup_driver():
    option = Options()
    option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=option)  # You can use any other browser driver you prefer
    print("setup driver")
    ts = TS(driver)
    print("initiate takescreenshot")
    ts.set_working_dir()
    print("Bikin directory baru")
    yield driver, ts
    print("PDF generate")
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    print("Click hamburger button")
    # driver.find_element(By.ID, "logout_sidebar_link").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()
    print("Click Logout link on sidebar")
    actual_url = driver.current_url
    assert actual_url == url, f"Expected URL: {url}, Actual URL: {actual_url}"
    driver.quit()
    print("yield driver quit on setup_driver")


@pytest.fixture
def setup_onboarding(setup_driver):
    driver = setup_driver
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    print("goto url website")
    # Perform login activity
    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    print("input user name")
    password_input.send_keys("secret_sauce")
    print("input password")
    login_button.click()
    print("click login button")
    return driver


@pytest.fixture
def tear_onboarding(setup_onboarding):
    driver = setup_onboarding
    # Open a new tab on the same browser and get its URL for the next test cases
    handles_before = driver.window_handles
    driver.execute_script("window.open('', '_blank');")
    handles_after = driver.window_handles
    new_tab_handle = [handle for handle in handles_after if handle not in handles_before][0]
    driver.switch_to.window(new_tab_handle)
    yield driver.current_url


@pytest.fixture
def tear_down(setup_driver):
    yield
    setup_driver.quit()
    print("yield driver quit on tear_down")
