import allure
from pages.elements import ListContentElement

from .base_page import BasePage


class ListContentMenu(BasePage):
    """Class to interact with List Content Menu"""

    @allure.step('Add new product to shopping list')
    def add_new_product_to_list(self, name: str):
        self.driver.find_element(*ListContentElement.INPUT_FIELD).send_keys(name)
        self.driver.find_element(*ListContentElement.PLUS_BUTTON).click()

    @allure.step('Check product presence in shopping list')
    def check_product_presence(self, name: str):
        all_items = self.driver.find_elements(*ListContentElement.LIST_ITEM)
        list_names = [item.text for item in all_items]
        assert (name in list_names)


    def add_new_product_with_properties(self, name: str, price: float, amount: float,
                                        amount_unit: str, ):
        pass
