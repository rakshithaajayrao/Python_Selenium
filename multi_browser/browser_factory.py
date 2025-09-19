from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

class BrowserFactory:
    def __init__(self, browser_type="chrome"):
        self.browser_type = browser_type.lower()

    def get_driver(self):
        if self.browser_type == "chrome":
            options = ChromeOptions()
            driver = webdriver.Chrome(service=ChromeService(), options=options)

        elif self.browser_type == "firefox":
            options = FirefoxOptions()
            driver = webdriver.Firefox(service=FirefoxService(), options=options)

        elif self.browser_type == "edge":
            options = EdgeOptions()
            driver = webdriver.Edge(service=EdgeService(), options=options)

        else:
            raise ValueError(f"Unsupported browser: {self.browser_type}")

        driver.maximize_window()
        return driver