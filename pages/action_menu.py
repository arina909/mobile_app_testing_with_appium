import allure
from pages.my_list_menu import MyListMenu
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .elements import ActionMenuElement, HeaderElement

PADE_LOAD_TIME = 10  # sec


class ActionMenu(BasePage):
    """Class to interact with Actions Menu"""

    @allure.step('Open action menu')
    def open_action_menu(self):
        self.driver.find_element(*HeaderElement.ACTION_MENU).click()
        return ActionMenu(self.driver)

    @allure.step('Choose My List option')
    def click_my_list_option(self):
        WebDriverWait(self.driver, PADE_LOAD_TIME).until(
            EC.visibility_of_element_located(ActionMenuElement.MY_LIST))
        self.driver.find_element(*ActionMenuElement.MY_LIST).click()
        return MyListMenu(self.driver)
