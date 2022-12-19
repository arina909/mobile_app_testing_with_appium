from time import sleep

from appium.webdriver.common.appiumby import AppiumBy

from .base_page import BasePage
from .elements import ChatElement


class ChatMenu(BasePage):
    """Class to interact with Chat Menu"""

    def click_login_button(self):
        sleep(5)
        elem = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        text = [elememt.text for elememt in elem]
        self.driver.find_element(ChatElement.LOGIN).click()
