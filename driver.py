from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
#from selenium.webdriver.opera.options import Options as OperaOptions


class Driver:
    def __init__(self, browser='chrome', port="9100"):
        self.browser = browser.lower()  # Normalize the browser name to lowercase
        self.port = port
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

    def quit(self):
        """Closes the browser."""
        self.driver.quit()

