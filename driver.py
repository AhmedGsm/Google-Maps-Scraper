from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
#from selenium.webdriver.opera.options import Options as OperaOptions

import time
import socket
from selenium.common.exceptions import WebDriverException

class Driver:
    def __init__(self, browser='chrome'):
        self.browser = browser.lower()  # Normalize the browser name to lowercase
        self.driver = self._create_driver()

    def _create_driver(self):
        """Creates a WebDriver instance based on the selected browser."""
        if self.browser == 'chrome':
            return self._create_chrome_driver()
        elif self.browser == 'firefox':
            return self._create_firefox_driver()
        elif self.browser == 'edge':
            return self._create_edge_driver()
        elif self.browser == 'opera':
            return self._create_opera_driver()
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")

    def _create_chrome_driver(self):
        chrome_options = ChromeOptions()
        # Add Chrome-specific options if necessary
        return webdriver.Chrome(options=chrome_options)

    def _create_firefox_driver(self):
        firefox_options = FirefoxOptions()
        # Add Firefox-specific options if necessary
        return webdriver.Firefox(options=firefox_options)

    def _create_edge_driver(self):
        edge_options = EdgeOptions()
        # Add Edge-specific options if necessary
        return webdriver.Edge(options=edge_options)

    def _create_opera_driver(self):
        opera_options = OperaOptions()
        # Add Opera-specific options if necessary
        return webdriver.Opera(options=opera_options)

    def get(self, url):
        """Navigates the browser to the specified URL."""
        self.driver.get(url)

    def land_page_url(self, url):
       #self.get(url)
       self.safe_get(url)
       try:
           self.maximize_window()
       except:
           print("The Browser is already maximized or the feature is not supported!")

    # Function to check internet connection
    def is_connected(self):
        try:
            # Try to connect to a known public server (Google's public DNS)
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            return True
        except OSError:
            return False

    def safe_get(self, url):
        while True:
            if self.is_connected():
                try:
                    self.get(url)
                    print("Page loaded successfully.")
                    break  # Exit the loop if the page is loaded
                except WebDriverException as e:
                    print(f"Encountered an error: {e}")
                    # Optional: Add logging if needed
            else:
                print("No internet connection. Retrying in 30 seconds...")
                time.sleep(30)  # Wait for 30 seconds before retrying

    def quit(self):
        """Closes the browser."""
        self.driver.quit()

