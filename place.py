from selenium.webdriver.common.by import By
from constants import *

class Place:
    def __init__(self, driver):
        self.driver = driver
        self.details = self.driver.find_elements(By.CSS_SELECTOR, PLACE_DETAILS_SELECTOR)
        pass

    def scrape_location(self):
        value = self.details[0]
        return value

    def scrape_website(self):
        value = self.details[1]
        return value

    def scrape_phone_number(self):
        value = self.details[2]
        return value