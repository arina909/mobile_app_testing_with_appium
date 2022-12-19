import allure
from pages.main_menu import MainMenu


@allure.description(
    """
    Test to check impossible to log in with empty name
    Test steps:
    1. Open app
    2. Click CHAT WITH ENNGLISH LEARNERS
    3. Click LOGIN
    """)
def test_check_impossible_to_log_in_with_empty_name(driver):
    main_menu = MainMenu(driver)
    chat_menu = main_menu.open_chat_with_learners()
    chat_menu.click_login_button()
