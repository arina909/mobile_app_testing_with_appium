from appium.webdriver.common.appiumby import AppiumBy


class HeaderElement:
    ACTION_MENU = (AppiumBy.ID, 'com.slava.buylist:id/button1')
    TITLE = (AppiumBy.ID, 'com.slava.buylist:id/textView1')


class ActionMenuElement:
    MY_LIST = (AppiumBy.XPATH, '//*[contains(@text, "My List")]')


class MyListElement:
    LIST_ITEM = (AppiumBy.ID, 'com.slava.buylist:id/item')

