from selenium.webdriver.common.by import By
from utils.driver_setup import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_simple_alert():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(By.XPATH, '//button[text()="Click for JS Alert"]').click()

    alert = driver.switch_to.alert
    print("Simple Alert Text:", alert.text)

    alert.accept()

    result = wait.until(
        EC.visibility_of_element_located((By.ID, "result"))
    ).text

    print("Simple Alert Result:", result)

    driver.quit()


def test_confirm_alert():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(By.XPATH, '//button[text()="Click for JS Confirm"]').click()

    alert = driver.switch_to.alert
    print("Confirm Alert Text:", alert.text)

    # Test Cancel 
    alert.dismiss()

    result = wait.until(
        EC.visibility_of_element_located((By.ID, "result"))
    ).text

    print("Confirm Alert (Cancel):", result)

    driver.quit()


def test_prompt_alert():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    driver.find_element(By.XPATH, '//button[text()="Click for JS Prompt"]').click()

    alert = driver.switch_to.alert
    print("Prompt Alert Text:", alert.text)

    alert.send_keys("007")
    alert.accept()

    result = wait.until(
        EC.visibility_of_element_located((By.ID, "result"))
    ).text

    print("Prompt Alert Result:", result)

    driver.quit()


# Run all
test_simple_alert()
test_confirm_alert()
test_prompt_alert()