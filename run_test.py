import sys
import os
import time
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# اضافه کردن دایرکتوری جاری به sys.path برای اینکه utils پیدا شود
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils import driver_setup as d  # ایمپورت driver_session

driver = d.driver_session()


@pytest.mark.login
def test_open():
    # Create driver session once

    # انجام عملیات لاگین
    logo = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Brand Blu Logo EN")
    logo.click()

    select_env = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,
                                     value="APIM-UAT, https://apim-qa.sdb247.com/openapi/v0")
    select_env.click()

    dismiss_env = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Dismiss")
    dismiss_env.click()

    username = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
    username.clear()
    username.send_keys("saman.kh")

    password = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeSecureTextField")
    password.clear()
    password.send_keys("Ss123456")

    show_pass = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons General Eye Hide Regular")
    show_pass.click()

    login = driver.find_element(by=AppiumBy.IOS_CLASS_CHAIN,
                                value="**/XCUIElementTypeButton[`name == \"ورود به بلو\"`]")
    login.click()

    # صبر کردن برای نمایش داشبورد بعد از لاگین
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Icons_General_Home_Max_Regular"))
    )

    print("Login and Dashboard Passed")


@pytest.mark.dashboard
def test_dashboard():
    # Dashboard
    dashboard = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons_General_Home_Max_Regular")
    dashboard.click()
    print("Show Dashboard Passed")

    search = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons General Search Regular")
    search.click()
    print("Show Search Passed")

    back = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="خانه")
    back.click()
    print("Show Back Passed")

    time.sleep(2)


@pytest.mark.login
def test_transfer():
    # Transfer
    transfer = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons_General_Transfer_Max_Regular")
    transfer.click()
    print("Show Transfer Passed")
    time.sleep(2)


@pytest.mark.login
def test_payment():
    # Payment
    payment = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons_General_Market_Max_Regular")
    payment.click()
    print("Show Payment Passed")
    time.sleep(2)


@pytest.mark.login
def test_card():
    # Card
    card = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons_General_Card_Vertical_Max_Regular")
    card.click()
    print("Show Card Passed")
    time.sleep(10)


@pytest.mark.login
def test_setting():
    # Setting
    setting = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Icons_General_Profile_Max_Regular")
    setting.click()
    print("Show Setting Passed")
    time.sleep(2)

    # Otp Page handling (if needed)
    # Uncomment and adjust locators as needed
    # otp_input = driver.find_element(by=AppiumBy.CLASS_NAME, value="XCUIElementTypeTextField")
    # otp_input.send_keys("123456")

    time.sleep(5)
