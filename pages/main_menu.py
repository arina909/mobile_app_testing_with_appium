import allure
from pages.elements import MainMenuElement

from .base_page import BasePage
from .list_content_page import ListContentMenu


class MainMenu(BasePage):
    """Class to interact with Main Menu"""

    @allure.step('Check there are no shopping lists')
    def check_shopping_lists_absence(self):
        all_items = self.driver.find_elements(*MainMenuElement.LIST_ITEM)
        assert (bool(all_items) is False)

    @allure.step('Create new shopping list')
    def create_new_list(self, name: str):
        self.driver.find_element(*MainMenuElement.INPUT_FIELD).send_keys(name)
        self.driver.find_element(*MainMenuElement.PLUS_BUTTON).click()
        return ListContentMenu(self.driver)

    @allure.step('Check shopping list presence')
    def check_shopping_list_presence(self, name: str, expected: bool = True):
        self.wait_element_visible(MainMenuElement.LIST_ITEM)
        all_items = self.driver.find_elements(*MainMenuElement.LIST_ITEM)
        list_names = [item.text for item in all_items]
        assert ((name in list_names) == expected)

    def get_ordinal_list_number_by_name(self, name: str):
        all_items = self.driver.find_elements(*MainMenuElement.LIST_ITEM)
        for index, item in enumerate(all_items):
            if item.text == name:
                return index

    @allure.step('Change shopping list name')
    def change_shopping_list_name(self, current_name: str, new_name: str):
        current_list_index = self.get_ordinal_list_number_by_name(current_name)
        self.driver.find_elements(*MainMenuElement.EDIT_BUTTON)[current_list_index].click()
        self.wait_element_visible(MainMenuElement.EDITING_ALERT_TEXT_FIELD)
        text_field = self.driver.find_element(*MainMenuElement.EDITING_ALERT_TEXT_FIELD)
        text_field.clear()
        text_field.send_keys(new_name)
        self.driver.find_element(*MainMenuElement.ALERT_OK_BUTTON).click()
