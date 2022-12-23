import allure
from pages.header import Header

NEW_PRODUCT = 'new product'


@allure.description(
    """
    Test to check "My List" is empty by default 
    Test steps:
    1. Open app
    2. Click on action menu, choose My List option
    3. Check "My List" is empty
    """)
def test_my_list_empty(driver):
    header = Header(driver)
    action_menu = header.open_action_menu()
    my_list_menu = action_menu.click_my_list_option()
    my_list_menu.check_my_list_is_empty()


@allure.description(
    """
    Test to check "My List" is empty by default 
    Test steps:
    1. Open app
    2. Click on action menu, choose My List option
    3. Insert new product in My List
    4. Check product added
    """)
def test_add_new_product_to_my_list(driver):
    header = Header(driver)
    action_menu = header.open_action_menu()
    my_list_menu = action_menu.click_my_list_option()
    my_list_menu.add_new_product_to_list(NEW_PRODUCT)
    my_list_menu.check_product_presence(NEW_PRODUCT)


@allure.description(
    """
    Test to check Voice Search alert appeared by click on Voice Search button
    Test steps:
    1. Open app
    2. Click on action menu, choose My List option
    3. Click on Voice Search button
    4. Check Voice Search alert appeared
    """)
def test_check_voice_search_alert_presence(driver):
    header = Header(driver)
    action_menu = header.open_action_menu()
    my_list_menu = action_menu.click_my_list_option()
    my_list_menu.click_voice_search_button()
    my_list_menu.check_voice_search_alert_appeared()
