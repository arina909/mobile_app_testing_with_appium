from appium.webdriver.common.appiumby import AppiumBy


class HeaderElement:
    ACTION_MENU = (AppiumBy.ID, 'com.slava.buylist:id/button1')
    TITLE = (AppiumBy.ID, 'com.slava.buylist:id/textView1')


class MainMenuElement:
    INPUT_FIELD = (AppiumBy.ID, 'com.slava.buylist:id/editText1')
    LIST_ITEM = (AppiumBy.ID, 'com.slava.buylist:id/title')
    PLUS_BUTTON = (AppiumBy.ID, 'com.slava.buylist:id/button2')
    EDIT_BUTTON = (AppiumBy.ID, 'com.slava.buylist:id/imageView2')
    EDITING_ALERT_TEXT_FIELD = (AppiumBy.CLASS_NAME, 'android.widget.EditText')
    ALERT_OK_BUTTON = (AppiumBy.ID, 'android:id/button1')


class ActionMenuElement:
    MY_LIST = (AppiumBy.XPATH, '//*[contains(@text, "My List")]')


class MyListElement:
    LIST_ITEM = (AppiumBy.ID, 'com.slava.buylist:id/title')
    INPUT_FIELD = (AppiumBy.ID, 'com.slava.buylist:id/editText1')
    MICRO_OR_PLUS_BUTTON = (AppiumBy.ID, 'com.slava.buylist:id/button2')
    VOICE_SEARCH_ALERT_TITLE = (AppiumBy.ACCESSIBILITY_ID, 'Google logo')


class ListContentElement:
    INPUT_FIELD = (AppiumBy.ID, 'com.slava.buylist:id/editText1')
    LIST_ITEM = (AppiumBy.ID, 'com.slava.buylist:id/title')
    PLUS_OR_SAVE_BUTTON = (AppiumBy.ID, 'com.slava.buylist:id/button2')
    REMOVAL_ALERT_TITLE = (AppiumBy.ID, 'android:id/alertTitle')
    CONFIRM_REMOVE = (AppiumBy.ID, 'android:id/button1')
    DECLINE_REMOVE = (AppiumBy.ID, 'android:id/button2')


class ListContentOption:
    COPY = (AppiumBy.XPATH, '//*[contains(@text, "Copy")]')
    ADD_TO_MY_LIST = (AppiumBy.XPATH, '//*[contains(@text, "Add to my list")]')
    EDIT = (AppiumBy.XPATH, '//*[contains(@text, "Edit")]')
    REMOVE = (AppiumBy.XPATH, '//*[contains(@text, "Remove")]')
