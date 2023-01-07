# mobile_app_testing_with_appium
Test framework based on appium+python+allure for app created to work with shopping lists

**Practice task description:**
1) Choose one of the test apps from storage
2) Create test plan for chosen app (10-15 main tests scenario)
3)Create test framework based on:
- Appium
- Python
- Allure
4) All test code have to be in your Github repo
5) Create documentation for framework (README file with instructions for prerequisites and setup, description of project structure, how to run tests
6) Demo for mentor

**Prerequisites and Setup istructions:**
1) Python 3.10 (https://www.python.org/downloads/)
2) Appium Server (https://github.com/appium/appium-desktop/releases/tag/v1.22.3-4)
3) Android Studio (https://developer.android.com/studio/install)
4) Install android device emulator via device manager or plug real device (in my case Pixel_3a_API_33_x86_64 emulator worked perfectly)
5) Run android device (if you are working with emulator check plugged devices via cmd `adb devices` copy current device name)
6) Run appium server
7) Install requirements `pip install -r requirements.txt`

**How to run tests in project:**
0) Check current device name in conftest.py. If device name is not match with `CURRENT_DEVICE` change variable value to device name from Prerequisites and Setup istructions step 5
1) Run tests (example: `py.test my_list_menu_tests.py --alluredir=reports`)
2) Collect allure report (`allure serve reports`) and enjoy results!
