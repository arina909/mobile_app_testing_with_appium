import os.path as ph

import pytest
from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.elements import HeaderElement

PADE_LOAD_TIME = 10  # sec
LOCAL_HOST = 'http://localhost:4723/wd/hub'
CURRENT_DEVICE = 'emulator-5554'
APP_PATH = ph.join(ph.dirname(__file__), 'Shopping.apk')


@pytest.fixture(scope='session')
def driver(device_name: str = CURRENT_DEVICE, close_version_warning: bool = True):
    desired_cap = {
        'deviceName': device_name,
        'platformName': 'Android',
        'app': APP_PATH,
        'autoGrantPermissions': True,
        'fullReset': True,
        'autoAcceptAlerts': True
    }

    driver = webdriver.Remote(command_executor=LOCAL_HOST, desired_capabilities=desired_cap)
    if close_version_warning:
        driver.switch_to.alert.accept()
    WebDriverWait(driver, PADE_LOAD_TIME).until(
        EC.visibility_of_element_located(HeaderElement.TITLE))

    yield driver
    driver.quit()
