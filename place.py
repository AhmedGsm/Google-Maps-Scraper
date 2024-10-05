from selenium.webdriver.common.by import By
from constants import *

class Place:
    def __init__(self, driver):
        self.driver = driver
        self.details = self.driver.find_elements(By.CSS_SELECTOR, PLACE_DETAILS_SELECTOR)
        pass

    def scrape_address(self):
        return self.details[0].text

    def scrape_website(self):
        return self.details[2].text

    def scrape_phone_number(self):
        return self.details[3].text