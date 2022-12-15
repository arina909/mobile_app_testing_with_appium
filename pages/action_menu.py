from .base_page import BasePage
from .elements import MainPage

class ActionMenu(BasePage):
    """Class to interact with Actions Menu"""

    def open_action_menu(self):
        self.app.find_element(MainPage.ACTION_MENU)

    def check_app_version(self, version: str):
        actual_version = self.app.find_element(ACTION_MENU).text()
        assert(actual_version == version)
        