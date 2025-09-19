import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
import os
from selenium.webdriver.common.keys import Keys

# Add project root to sys.path so Python can find report_creator
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from report_creator.report_writer import ReportWriter
from browser_factory import BrowserFactory

test_name = "test_excelform"  
report = ReportWriter(test_name)

browser_type = "edge"
report.log("INFO", f"Browser: {browser_type}")

factory = BrowserFactory(browser_type)

driver = factory.get_driver()
report.log("INFO", "Driver initialized successfully")

# Load Excel data
df = pd.read_excel(r'C:\Users\raksh\Automation_Project\Git\Python_Selenium\TestData\Testdatatest.xlsx')

driver.get("https://demoqa.com/automation-practice-form")
report.log("PASS", "Navigated to Practice Form")
time.sleep(5)

# Loop through each row in Excel
for index, row in df.iterrows():
    # Fill form fields
    time.sleep(1)
    driver.find_element(By.ID, "firstName").clear()
    driver.find_element(By.ID, "firstName").send_keys(row['First Name'])
    report.log("PASS", f"First Name Entered: {row['First Name']}")

    driver.find_element(By.ID, "lastName").clear()
    driver.find_element(By.ID, "lastName").send_keys(row['Last Name'])
    report.log("PASS", f"Last Name Entered: {row['Last Name']}")
    
    driver.find_element(By.ID, "userEmail").clear()
    driver.find_element(By.ID, "userEmail").send_keys(row['Email'])
    report.log("PASS", f"Email Entered: {row['Email']}")

    # Gender selection
    gender_xpath = f"//label[text()='{row['Gender']}']"
    driver.find_element(By.XPATH, gender_xpath).click()
    report.log("FAIL",f"Selected not Gender - for demo purpose: {row['Gender']}")

    driver.find_element(By.ID, "userNumber").clear()
    driver.find_element(By.ID, "userNumber").send_keys(str(row['Mobile']))
    report.log("PASS", f"Mobile Number Entered: {row['Mobile']}")
    report.generate()

    # Submit the form
    #driver.find_element(By.ID, "submit").click()
    time.sleep(2)

    # Optional: Go back to form for next entry
    driver.get("https://demoqa.com/automation-practice-form")
    time.sleep(2)
    report.generate()

# Close browser
#driver.quit()