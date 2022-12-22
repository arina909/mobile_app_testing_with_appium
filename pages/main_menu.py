from .base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy


class MainMenu(BasePage):
    """Class to interact with Main Menu"""

    def create_new_list(self):
        self.driver
