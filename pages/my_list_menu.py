import allure

from .base_page import BasePage
from .elements import MyListElement, HeaderElement

PADE_LOAD_TIME = 10  # sec


class MyListMenu(BasePage):
    """Class to interact with My List Menu"""

    @allure.step('Check My List is empty')
    def check_my_list_is_empty(self):
        self.wait_element_visible(HeaderElement.TITLE)
        all_items = self.driver.find_elements(*MyListElement.LIST_ITEM)
        assert (bool(all_items) is False)
