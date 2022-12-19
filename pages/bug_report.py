from .base_page import BasePage
from .elements import MainPageElement, ActionMenuElement, BugReportElement
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

class BugReportMenu(BasePage):
    """Class to interact with Bug Report Menu"""

    def check_bug_reporting_notification_presence(self):
        self.driver.find_element(*BugReportElement.MESSAGE)

    def cancel_bug_reporting(self):
        sleep(5)
        elem = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")
        text = [elememt.text for elememt in elem]
        self.driver.find_element(*BugReportElement.CANCEL).click()