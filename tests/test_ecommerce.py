from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import get_driver

def test_add_to_cart():
    driver = get_driver()
    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    #login
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Product selection

    product = wait.until(
    EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    )
    product_name = product.text
    product.click()

    # Add to Cart
    wait.until(
        EC.element_to_be_clickable((By.ID, "add-to-cart"))
    ).click()

    # Go to Cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Verify product in cart
    cart_item = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
    ).text

    assert product_name == cart_item

    print("Add to cart Test: PASSED!!")

    driver.quit()


test_add_to_cart()