import pytest
from selenium import webdriver
from utilities.take_screenshot import TakeScreenshot

@pytest.mark.usefixtures("setup_onboarding")
class TestMultipleCases:
    driver = webdriver.Chrome()
    def test_addition(self):
        TakeScreenshot.
        # Your actual test case using the URL obtained from tear_onboarding fixture
        print("Test Case Addition")
        # print("URL from tear_onboarding fixture:", tear_onboarding)
        # Add your test logic here
        assert 1 + 1 == 2

    def test_subtraction(self):
        # Your actual test case using the URL obtained from tear_onboarding fixture
        print("Test Case Subtraction")
        # print("URL from tear_onboarding fixture:", tear_onboarding)
        # Add your test logic here
        assert 3 - 1 == 2
