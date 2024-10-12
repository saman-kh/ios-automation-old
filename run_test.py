from appium import webdriver  # Correct import for Appium WebDriver
from appium.options.common.base import AppiumOptions  # Import for Appium options
from appium.webdriver.common.appiumby import AppiumBy  # Correct import for finding elements

# Optional: Other necessary Selenium or Appium imports
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

import time

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

# Find and interact with elements
el1 = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeSecureTextField")
el1.send_keys("Yaali123456")
el2 = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN, value='**/XCUIElementTypeButton[`name == "ورود به بلو"`]')
el2.click()

time.sleep(5)


# Close the driver
driver.quit()
