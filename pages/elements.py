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


class ListContentElement:
    INPUT_FIELD = (AppiumBy.ID, 'com.slava.buylist:id/editText1')
    LIST_ITEM = (AppiumBy.ID, 'com.slava.buylist:id/title')
    PLUS_BUTTON = (AppiumBy.ID, 'com.slava.buylist:id/button2')
