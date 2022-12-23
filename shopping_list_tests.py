import allure
from pages.header import Header
from pages.main_menu import MainMenu

NEW_LIST = 'new list'
NEW_PRODUCT = 'new product'
NEWEST_LIST = 'newest list'


@allure.description(
    """
    Test to check there are no shopping lists by default 
    Test steps:
    1. Open app
    2. Check there are no lists
    """)
def test_shopping_lists_absence_by_default(driver):
    main_menu = MainMenu(driver)
    main_menu.check_shopping_lists_absence()


@allure.description(
    """
    Test to check possibility to create empty list
    Test steps:
    1. Open app
    2. Add new list 
    3. Without adding any product go back
    4. Check list presence
    """)
def test_possibility_to_create_empty_list(driver):
    main_menu = MainMenu(driver)
    list_content_menu = main_menu.create_new_list(NEW_LIST)
    list_content_menu.go_to_previous_page(hide_keyboard=True)
    main_menu.check_shopping_list_presence(NEW_LIST)


@allure.description(
    """
    Test to check possibility to create new list and add product
    Test steps:
    1. Open app
    2. Insert any list name and click Plus button and check title has list name
    3. Insert any product name, check product presence in list
    """)
def test_new_list_with_product_creation(driver):
    main_menu = MainMenu(driver)
    list_content_menu = main_menu.create_new_list(NEW_LIST)
    Header(driver).check_header_title(NEW_LIST)
    list_content_menu.add_new_product_to_list(NEW_PRODUCT)
    list_content_menu.check_product_presence(NEW_PRODUCT)


@allure.description(
    """
    Test to check possibility to change shopping list name
    Test steps:
    1. Open app
    2. Add new list, without adding any product go back
    3. Click on Pencil button and insert new name 
    4. Check name is changed
    """)
def test_shopping_list_renaming(driver):
    main_menu = MainMenu(driver)
    list_content_menu = main_menu.create_new_list(NEW_LIST)
    list_content_menu.go_to_previous_page(hide_keyboard=True)
    main_menu.change_shopping_list_name(NEW_LIST, NEWEST_LIST)
    main_menu.check_shopping_list_presence(NEWEST_LIST)
    main_menu.check_shopping_list_presence(NEW_LIST, expected=False)
