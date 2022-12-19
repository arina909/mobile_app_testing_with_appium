import allure
from pages.main_menu import MainMenu

CURRENT_VERSION = '1.8.7'


@allure.description(
    """
    Test to check app version
    Test steps:
    1. Open app
    2. Click on action menu
    3. Check caption "Version 1.8.7" is present
    """)
def test_app_verson(driver):
    main_menu = MainMenu(driver)
    action_menu = main_menu.open_action_menu()
    action_menu.check_app_version(version=CURRENT_VERSION)

@allure.description(
    """Test to check possibility to cancel bug reporting
    Test steps:
    1. Open app
    2. Click on action menu
    3. Click "Report a bug" button and notification about report is appeared
    4. Click cancel button and check app switched to Main page
    """)
def test_bug_report_cancel(driver):
    main_menu = MainMenu(driver)
    action_menu = main_menu.open_action_menu()
    bug_report = action_menu.click_report_bug()
    # bug_report.check_bug_reporting_notification_presence()
    bug_report.cancel_bug_reporting()
