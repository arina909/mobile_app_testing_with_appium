from pages.bug_report import BugReportMenu
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep

from .base_page import BasePage
from .elements import ActionMenuElement, BugReportElement

PADE_LOAD_TIME = 10 #  sec

class ActionMenu(BasePage):
    """Class to interact with Actions Menu"""

    def check_app_version(self, version: str):
        version_elem_text = self.driver.find_element(*ActionMenuElement.VERSION).text
        actual_version = version_elem_text.replace('Version ', '')
        assert(actual_version == version)

    def click_report_bug(self):
        self.driver.find_element(*ActionMenuElement.REPORT_BUG).click()
        return BugReportMenu(self.driver)
