from utilities.logger import get_logger

log = get_logger()

def test_login(driver):

    log.info("Opening website")

    driver.get("https://automationexercise.com")

    log.info("website opened successfully!!")