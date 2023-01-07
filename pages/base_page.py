import allure
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from waiting import wait

PADE_LOAD_TIME = 10  # sec


class BasePage:
    """Class with common actions"""

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Go back to previous page')
    def go_to_previous_page(self, hide_keyboard: bool = False):
        if hide_keyboard:
            self.hide_keyboard()
        self.driver.back()

    @allure.step('Wait until element is visible')
    def wait_element_visible(self, element):
        WebDriverWait(self.driver, PADE_LOAD_TIME).until(
            EC.visibility_of_element_located(element))

    @allure.step('Hide keyboard')
    def hide_keyboard(self):
        wait(lambda: self.driver.is_keyboard_shown(),
             timeout_seconds=PADE_LOAD_TIME)
        self.driver.hide_keyboard()

    @allure.step('Perform Long Press')
    def long_press(self, element):
        TouchAction(self.driver).long_press(element).perform()
