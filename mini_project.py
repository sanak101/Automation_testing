from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

def test_valid_login():
    driver = webdriver.Chrome(service=Service())
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/login")

    wait.until(EC.visibility_of_element_located((By.ID,"username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CLASS_NAME, "radius").click()

    success_msg = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    print("valid login test:", "Passed" if "You logged into a secure area!" in success_msg else "Failed")

    driver.quit()

def test_invalid_login():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/login")

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("mrsmith")
    driver.find_element(By.ID, "password").send_keys("Wrongpass")
    driver.find_element(By.CLASS_NAME, "radius").click()

    error_msg = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    print("invalid login test:", "Passed" if "Your username is invalid!" in error_msg else "Failed")

    driver.quit()


test_valid_login()
test_invalid_login()