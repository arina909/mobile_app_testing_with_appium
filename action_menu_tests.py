from pages.action_menu import ActionMenu
def test_app_verson(app):
    """Test to check schema version
    Test steps
    1. Open app
    2. Click on action menu
    3. Check caption "Version 1.8.7" is present
    """
    app = ActionMenu(app)
    app.open_action_menu()
    app.check_app_version('1.8.7')