from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
#from selenium.webdriver.opera.options import Options as OperaOptions

import time
import socket
from selenium.common.exceptions import WebDriverException

class DriverManipulator():
    def __init__(self, browser='chrome'):
        self.browser = browser.lower()  # Normalize the browser name to lowercase
        self.driver = None
        self.is_fast_scraping = True
        self._create_driver()

    def _create_driver(self):
        """Creates a WebDriver instance based on the selected browser."""
        if self.browser == 'chrome':
            self._create_chrome_driver()
        elif self.browser == 'firefox':
            self._create_firefox_driver()
        elif self.browser == 'edge':
            self._create_edge_driver()
        elif self.browser == 'opera':
            self._create_opera_driver()
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")

    def _create_chrome_driver(self):
        if self.is_fast_scraping:
            # Add Chrome-specific options for fast scraping
            chrome_options = ChromeOptions()
            prefs = {
                "profile.default_content_setting_values": {
                    "images": 2,  # 2: Block all images
                    # "javascript": 2,  # Optional: Block JavaScript (if not needed)
                    "plugins": 2,  # Optional: Block plugins
                    "geolocation": 2,  # Block geolocation requests
                    "notifications": 2,  # Block notifications
                }
            }

            # Add the prefs to Chrome options
            chrome_options.add_experimental_option("prefs", prefs)
            chrome_options.add_argument("--disable-notifications")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")  # Helps with memory usage in containers
            chrome_options.add_argument("--disable-extensions")  # Optional: Disables extensions to avoid conflicts        self.driver = webdriver.Chrome(options=chrome_options)

            self.driver = webdriver.Chrome(options=chrome_options)
    def _create_firefox_driver(self):
        if self.is_fast_scraping:
            firefox_options = FirefoxOptions()
            # Add Chrome-specific options for fast scraping
            firefox_options = FirefoxOptions()

            # Create a Firefox Profile
            profile = webdriver.FirefoxProfile()

            # Disable image loading
            profile.set_preference("permissions.default.image", 2)  # Block all images

            # Disable JavaScript (optional)
            # profile.set_preference("javascript.enabled", False)

            # Disable plugins
            profile.set_preference("plugin.state.flash", 0)  # Block flash plugins
            profile.set_preference("dom.ipc.plugins.enabled.libflashplayer.so", "false")

            # Disable geolocation requests
            profile.set_preference("geo.enabled", False)

            # Block notifications
            profile.set_preference("dom.webnotifications.enabled", False)

            # Add arguments for better performance (optional)
            firefox_options.add_argument("--disable-gpu")  # Disable GPU (optional, for containers)
            firefox_options.add_argument("--no-sandbox")  # Disable sandbox (useful in Docker containers)

            # Disable extensions
            firefox_options.add_argument("--disable-extensions")

            # Run Firefox in headless mode (optional)
            # firefox_options.add_argument("--headless")

            self.driver = webdriver.Firefox(options=firefox_options)
            return
        # Assign the driver to firefox
        self.driver = webdriver.Firefox()

        #self.driver = webdriver.Firefox(options=firefox_options)

    def _create_edge_driver(self):
        edge_options = EdgeOptions()
        # Add Edge-specific options if necessary
        self.driver = webdriver.Edge(options=edge_options)

    def _create_opera_driver(self):
        opera_options = OperaOptions()
        # Add Opera-specific options if necessary
        self.driver = webdriver.Opera(options=opera_options)

    """def get(self, url):
        
        self.get(url)"""

    def land_page_url(self, url):
       #self.get(url)
       self.safe_get(url)
       """try:
           self.driver.maximize_window()
       except:
           print("The Browser is already maximized or the feature is not supported!")"""

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
                    self.driver.get(url)
                    print("Page loaded successfully.")
                    break  # Exit the loop if the page is loaded
                except WebDriverException as e:
                    print(f"Encountered an error: {e}")
                    # Optional: Add logging if needed
            else:
                print("No internet connection. Retrying in 30 seconds...")
                time.sleep(30)  # Wait for 30 seconds before retrying

    def quit_driver(self):
        """Closes the browser."""
        self.driver.quit()

