import time
from appium import webdriver  # Correct import for Appium WebDriver
from appium.options.common.base import AppiumOptions  # Import for Appium options
from appium.webdriver.common.appiumby import AppiumBy  # Correct import for finding elements

# Optional: Other necessary Selenium or Appium imports
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

def test_open():
    # Set up your Appium options and capabilities
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "iOS",
        "appium:udid": "00008101-001C58560106001E",
        "appium:automationName": "XCUITest",
        "appium:bundleId": "com.blubank.app-dev",
        "appium:includeSafariInWebviews": True,
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True,
        "appium:showXcodeLog": True,
        "appium:wdaStartupRetries": 3,
        "appium:wdaStartupRetryInterval": 20000,
        "appium:clearSystemFiles": True
    })

    # Create a new Appium WebDriver session using the correct 'webdriver.Remote' call
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    # select UAT env
    logo = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Brand Blu Logo EN")
    logo.click()
    select_env = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                     value="APIM-UAT, https://apim-qa.sdb247.com/openapi/v0")
    select_env.click()
    dismiss_env = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Dismiss")
    dismiss_env.click()

    # Login
    username = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
    username.clear()
    username.send_keys("saman.kh")
    password = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeSecureTextField")
    time.sleep(.5)
    password.clear()
    password.send_keys("Ss123456")
    time.sleep(.5)
    show_pass = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons General Eye Hide Regular")
    show_pass.click()
    login = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN,
                                value="**/XCUIElementTypeButton[`name == \"ورود به بلو\"`]")
    login.click()
    time.sleep(2)
    print("Login Passed")

    # Dashboard
    dashboard = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons_General_Home_Max_Regular")
    dashboard.click()
    print("Show Dashboard Passed")

    time.sleep(2)

    # Transfer
    transfer = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons_General_Transfer_Max_Regular")
    transfer.click()
    print("Show Transfer Passed")

    time.sleep(2)

    # Payment
    payment = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons_General_Market_Max_Regular")
    payment.click()
    print("Show Payment Passed")

    time.sleep(2)

    # Card
    # card = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons_General_Card_Vertical_Max_Regular")
    # card.click()
    # print("Show Card Passed")

    time.sleep(10)

    # # Setting
    setting = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons_General_Profile_Max_Regular")
    setting.click()
    print("Show Setting Passed")

    time.sleep(2)

    # Otp Page
    # el10 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[6]/XCUIElementTypeStaticText")
    # el10.send_keys("1")
    # el11 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[5]/XCUIElementTypeStaticText")
    # el11.send_keys("1")
    # el12 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[4]/XCUIElementTypeStaticText")
    # el12.send_keys("1")
    # el13 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[3]/XCUIElementTypeStaticText")
    # el13.send_keys("1")
    # el14 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeStaticText")
    # el14.send_keys("1")
    # el15 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value="**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeTextView/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeStaticText")
    # el15.send_keys("1")

    time.sleep(5)

    # Close the driver
    driver.quit()
