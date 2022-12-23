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

    @allure.step('Add new product to My List')
    def add_new_product_to_list(self, name: str):
        self.driver.find_element(*MyListElement.INPUT_FIELD).send_keys(name)
        self.driver.find_element(*MyListElement.MICRO_OR_PLUS_BUTTON).click()

    @allure.step('Check product presence in shopping list')
    def check_product_presence(self, name: str):
        all_items = self.driver.find_elements(*MyListElement.LIST_ITEM)
        list_names = [item.text for item in all_items]
        assert (name in list_names)

    @allure.step('Click on Voice Search button')
    def click_voice_search_button(self):
        self.driver.find_element(*MyListElement.MICRO_OR_PLUS_BUTTON).click()

    @allure.step('Check Google Voice Search Alert appeared')
    def check_voice_search_alert_appeared(self):
        self.wait_element_visible(MyListElement.VOICE_SEARCH_ALERT_TITLE)
        present = self.driver.find_element(*MyListElement.VOICE_SEARCH_ALERT_TITLE).is_displayed()
        assert (present is True)
