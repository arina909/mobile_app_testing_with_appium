import allure
from pages.action_menu import ActionMenu

from .base_page import BasePage
from .elements import HeaderElement


class Header(BasePage):
    """Class to interact with Actions Menu"""

    @allure.step('Open action menu')
    def open_action_menu(self):
        self.driver.find_element(*HeaderElement.ACTION_MENU).click()
        return ActionMenu(self.driver)

    @allure.step('Check header title')
    def check_header_title(self, title):
        self.wait_element_visible(HeaderElement.TITLE)
        actual_header = self.driver.find_element(*HeaderElement.TITLE).text
        assert (title == actual_header)
