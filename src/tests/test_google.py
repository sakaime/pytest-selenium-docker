import os
from datetime import datetime

from selenium import webdriver

class TestGoogle:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Remote(
            command_executor="http://browser:4444/wd/hub",
            options=webdriver.ChromeOptions(),
        )

    def test_access_google(self):
        driver = TestGoogle.driver

        file_name = datetime.now().strftime("%y%m%d_%H%M%S.png")
        screenshot_path = os.path.join("/root/src/screenshots", file_name)

        driver.get("https://www.google.com/")
        driver.get_screenshot_as_file(screenshot_path)

        assert driver.current_url == "https://www.google.com/"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()