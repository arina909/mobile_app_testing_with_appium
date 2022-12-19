import allure
from pages.action_menu import ActionMenu
from pages.chat_menu import ChatMenu

from .base_page import BasePage
from .elements import MainPageElement


class MainMenu(BasePage):
    """Class to interact with Main Menu"""

    @allure.step('Open action menu')
    def open_action_menu(self):
        self.driver.find_element(*MainPageElement.ACTION_MENU).click()
        return ActionMenu(self.driver)

    @allure.step('Click on Chat with English learners button')
    def open_chat_with_learners(self):
        self.driver.find_element(*MainPageElement.CHAT).click()
        return ChatMenu(self.driver)

    @allure.step('Check Main Page is opened')
    def check_main_page_is_opened(self):
        self.driver.find_element(*MainPageElement.CHOOSE_LEVEL).is_displayed()