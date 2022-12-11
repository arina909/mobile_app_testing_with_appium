import pytest
from appium import webdriver
from pages.elements import OpeningWarning, MainPage
from selenium.webdriver.support import expected_conditions as ECimport
import os.path as ph


LOCAL_HOST = 'http://localhost:4723/wd/hub'
CURRENT_DEVICE = 'emulator-5554'

@pytest.fixture(scope='session')
def app(device_name: str = CURRENT_DEVICE, close_version_warning: bool = True):
    desired_cap = {
      'deviceName': device_name,
      'platformName': 'Android',
      'app': 'EnglishGrammar.apk',
      'autoGrantPermissions': True,
      'fullReset': True
    }

    driver = webdriver.Remote(command_executor=LOCAL_HOST, desired_capabilities=desired_cap)
    if close_version_warning:
        driver.find_element(OpeningWarning.OK_BUTTON).click()
    wait.until(EC.element_to_be_clickable(MainPage.ACTION_MENU))