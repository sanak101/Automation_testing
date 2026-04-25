from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.driver_setup import get_driver

def test_valid_login():
    driver = get_driver()
    wait = WebDriverWait(driver,10)

    driver.get("https://the-internet.herokuapp.com/login")

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CLASS_NAME, "radius").click()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    driver.quit()



def test_invalid_login():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/login")

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("wrong")
    driver.find_element(By.CLASS_NAME, "radius").click()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    print("Invalid Login:", "PASS" if "invalid" in message else "FAIL")

    driver.quit()


test_valid_login()
test_invalid_login()