import pytest
from utils.driver_setup import get_driver

@pytest.fixture(scope="session")
def driver():
    driver = get_driver()

    yield driver

    driver.quit()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login(driver):   # 👈 pass fixture here
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/login")

    wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CLASS_NAME, "radius").click()

    message = wait.until(
        EC.visibility_of_element_located((By.ID, "flash"))
    ).text

    assert "secure area" in message