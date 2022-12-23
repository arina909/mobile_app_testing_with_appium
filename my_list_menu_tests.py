import allure
from pages.header import Header


@allure.description(
    """
    Test to check "My List" is empty by default 
    Test steps:
    1. Open app
    2. Click on action menu
    3. Check  "My List" is empty
    """)
def test_my_list_empty(driver):
    header = Header(driver)
    action_menu = header.open_action_menu()
    my_list_menu = action_menu.click_my_list_option()
    my_list_menu.check_my_list_is_empty()
