from appium import webdriver
from appium.options.common.base import AppiumOptions


def driver_session():
    # تنظیمات Appium
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "iOS",
        "appium:udid": "00008101-001C58560106001E",
        "appium:automationName": "XCUITest",
        "appium:bundleId": "com.blubank.app-dev",
        "appium:newCommandTimeout": 3600,
    })

    # ایجاد سشن درایور
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    return driver
