import allure
from pages.my_list_menu import MyListMenu

from .base_page import BasePage
from .elements import ActionMenuElement, HeaderElement


class ActionMenu(BasePage):
    """Class to interact with Actions Menu"""

    @allure.step('Open action menu')
    def open_action_menu(self):
        self.driver.find_element(*HeaderElement.ACTION_MENU).click()
        return ActionMenu(self.driver)

    @allure.step('Choose My List option')
    def click_my_list_option(self):
        self.wait_element_visible(ActionMenuElement.MY_LIST)
        self.driver.find_element(*ActionMenuElement.MY_LIST).click()
        return MyListMenu(self.driver)
