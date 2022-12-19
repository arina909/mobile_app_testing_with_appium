from appium.webdriver.common.appiumby import AppiumBy

class MainPageElement():
    ACTION_MENU = (AppiumBy.XPATH, '//*[contains(@text, "menu_dots")]')
    CHOOSE_LEVEL = (AppiumBy.XPATH, '//*[contains(@text, "CHOOSE A LEVEL")]')
    CHAT = (AppiumBy.XPATH, '//android.view.View[@content-desc="CHAT WITH ENGLISH LEARNERS"]')

class ActionMenuElement():
    VERSION = (AppiumBy.XPATH, '//*[contains(@text, "Version")]')
    REPORT_BUG = (AppiumBy.XPATH, '//android.view.View[@content-desc="Report a bug"]')

class BugReportElement():
    MESSAGE = (AppiumBy.XPATH, '//*[contains(@text, "Hi!")]')
    CANCEL = (AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View/android.widget.Button[1]')

class ChatElement():
    LOGIN = (AppiumBy.XPATH, '//*[contains(@text, "Login")]')