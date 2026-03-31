from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

# Remove ads

# driver.execute_script("""document.querySelector('footer').style.display = 'none';
# document.getElementById('fixedban').style.display='none';""")

driver.execute_script("""
var footer = document.querySelector('footer');
if (footer) {
    footer.style.display = 'none';
}

var ad = document.getElementById('fixedban');
if (ad) {
    ad.style.display = 'none';
}
""")

# First Name
wait.until(EC.visibility_of_element_located((By.ID, "firstName"))).send_keys("John")

# Last Name
driver.find_element(By.ID, "lastName").send_keys("Smith")

# Email
driver.find_element(By.ID, "userEmail").send_keys("john.smith@test.com")

# Gender
gender = driver.find_element(By.XPATH, "//label[text()='Male']")
driver.execute_script("arguments[0].click();", gender)

#Mobile
driver.find_element(By.ID, "userNumber").send_keys("03123456789")

# Date of Birth
driver.find_element(By.ID, "dateOfBirthInput").click()
driver.find_element(By.CLASS_NAME, "react-datepicker__year-select").send_keys("1998")
driver.find_element(By.CLASS_NAME, "react-datepicker__month-select").send_keys("may")
driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day--015')]").click()

# Subjects
subjects = driver.find_element(By.ID, "subjectsInput")
subjects.send_keys("Computer Science")
subjects.send_keys(Keys.ENTER)

# hobbies 
hobby = driver.find_element(By.XPATH, "//label[text()='Reading']")
driver.execute_script("arguments[0].click();", hobby)


# 🔹 Address
driver.find_element(By.ID, "currentAddress").send_keys("Karachi, Pakistan")

# 🔹 State
state = driver.find_element(By.ID, "react-select-3-input")
state.send_keys("NCR")
state.send_keys(Keys.ENTER)

# 🔹 City
city = driver.find_element(By.ID, "react-select-4-input")
city.send_keys("Delhi")
city.send_keys(Keys.ENTER)

# 🔹 Scroll to submit
submit_btn = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].scrollIntoView();", submit_btn)

# 🔹 Submit
driver.execute_script("arguments[0].click();", submit_btn)


time.sleep(5)
driver.quit()