from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_cap = {
  'deviceName': 'emulator-5556',
  'platformName': 'Android',
  'app': 'C:\\Users\\asverchkova\\Downloads\\EnglishGrammar.apk',
  'autoGrantPermissions': True,
  'fullReset': True
}
localhost = 'http://localhost:4723/wd/hub'

driver = webdriver.Remote(command_executor=localhost, desired_capabilities=desired_cap)
driver.implicitly_wait()

driver.find_element(AppiumBy.ID, 'android:id/button1').click()
wait.until(EC.element_to_be_clickable((By.XPATH,'//UIAApplication[1]/UIAWindow[1]/UIAButton[@text="example text"]')))