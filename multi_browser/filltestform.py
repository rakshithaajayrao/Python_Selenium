import sys
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Add project root to sys.path so Python can find report_creator
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from report_creator.report_writer import ReportWriter
from browser_factory import BrowserFactory

test_name = "test_qaform"  
report = ReportWriter(test_name)

browser_type = "edge"
report.log("INFO", f"Browser: {browser_type}")

factory = BrowserFactory(browser_type)

driver = factory.get_driver()
report.log("INFO", "Driver initialized successfully")

""" driver.get("https://demoqa.com")  
# Step 2: Search for a section (e.g., "Practice Form")
search_box = driver.find_element(By.CLASS_NAME, "header-search")
search_box.click()
search_box.send_keys("Practice Form") """

time.sleep(2)  # Wait for results to load

# Step 3: Navigate to the Practice Form page
driver.get("https://demoqa.com/automation-practice-form")
time.sleep(2)  # Wait for results to load

# Step 4: Fill out the form (simulate adding an application)
driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")
driver.find_element(By.ID, "userEmail").send_keys("john.doe@example.com")
driver.find_element(By.XPATH, "//label[text()='Male']").click()
driver.find_element(By.ID, "userNumber").send_keys("1234567890")

report.log("PASS", "John, Doe, EmailID, Gender, PhoneNumber Entered")
report.generate()
# Step 5: Submit the form
#driver.find_element(By.ID, "submit").click()
report.log("FAIL", "Submit button not clicked - for demo purpose")
report.generate()

# Step 6: Wait and close
time.sleep(3)
#driver.quit()

