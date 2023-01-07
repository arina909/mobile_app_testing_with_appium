import allure
from pages.elements import ListContentElement, ListContentOption
from .base_page import BasePage


class ListContentMenu(BasePage):
    """Class to interact with List Content Menu"""

    @allure.step('Add new product to shopping list')
    def add_new_product_to_list(self, name: str):
        self.wait_element_visible(ListContentElement.INPUT_FIELD)
        self.driver.find_element(*ListContentElement.INPUT_FIELD).send_keys(name)
        self.driver.find_element(*ListContentElement.PLUS_OR_SAVE_BUTTON).click()

    @allure.step('Check product presence in shopping list')
    def check_product_presence(self, name: str, expected: bool = True):
        all_items = self.driver.find_elements(*ListContentElement.LIST_ITEM)
        list_names = [item.text for item in all_items]
        assert ((name in list_names) == expected)

    def get_product_number_by_name(self, name: str):
        all_items = self.driver.find_elements(*ListContentElement.LIST_ITEM)
        for index, item in enumerate(all_items):
            if item.text == name:
                return index

    @allure.step('Choose option to manipulate with product')
    def _choose_option_in_product_menu(self, product: str, option: ListContentOption):
        product_to_click = self.get_product_number_by_name(product)
        self.long_press(self.driver.find_elements(*ListContentElement.LIST_ITEM)[product_to_click])
        self.wait_element_visible(option)
        self.driver.find_element(*option).click()

    @allure.step('Change product name')
    def change_product_name(self, current_name: str, new_name: str):
        self._choose_option_in_product_menu(current_name, ListContentOption.EDIT)
        text_field = self.driver.find_element(*ListContentElement.INPUT_FIELD)
        text_field.clear()
        text_field.send_keys(new_name)
        self.driver.find_element(*ListContentElement.PLUS_OR_SAVE_BUTTON).click()

    @allure.step('Delete product from list')
    def delete_product_from_list(self, product_name: str):
        self._choose_option_in_product_menu(product_name, ListContentOption.REMOVE)
        self.wait_element_visible(ListContentElement.REMOVAL_ALERT_TITLE)
        self.driver.find_element(*ListContentElement.CONFIRM_REMOVE).click()

    @allure.step('Decline product deletion from list')
    def decline_product_deletion(self, product_name: str):
        self._choose_option_in_product_menu(product_name, ListContentOption.REMOVE)
        self.wait_element_visible(ListContentElement.REMOVAL_ALERT_TITLE)
        self.driver.find_element(*ListContentElement.DECLINE_REMOVE).click()
