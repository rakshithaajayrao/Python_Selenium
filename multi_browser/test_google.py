import sys
import os
import time

# Add project root to sys.path so Python can find report_creator
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from report_creator.report_writer import ReportWriter
from browser_factory import BrowserFactory

#print("sys.path:", sys.path)
#print("Looking for report_creator in:", project_root)

test_name = "test_google"  #  Define test_name before using it
report = ReportWriter(test_name)

# Choose browser: "chrome", "firefox", or "edge"
browser_type = "edge"
report.log("INFO", f"Browser: {browser_type}")

factory = BrowserFactory(browser_type)

try:
    driver = factory.get_driver()
    report.log("INFO", "Driver initialized successfully")

    driver.get("https://www.google.com")
    title = driver.title

    if "Google" in title:
        report.log("PASS", f"Title matched: {title}")
    else:
        report.log("FAIL", f"Unexpected title: {title}")

    time.sleep(2)

except Exception as e:
    report.log("FAIL", f"Exception occurred: {str(e)}")

finally:
    driver.quit()
    report.log("FAIL", "Driver closed ==> Fail status for demo purposes")
    report.generate()