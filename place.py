import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import *

class Place:
    def __init__(self, driver):
        self.driver = driver
        self.website = "?"
        self.phone_number = "?"
        self.initializations(driver)

    def initializations(self, driver):
        # Find elements to pick 6th element that contains places details
        elements = driver.find_elements(By.CSS_SELECTOR, PLACE_DETAILS_CONTAINER_SELECTOR)
        # Wait until 8 element are found
        while len(elements) < 6:
            elements = driver.find_elements(By.CSS_SELECTOR, PLACE_DETAILS_CONTAINER_SELECTOR)
            print("Elements are < 8, waiting element to be loaded...")
            time.sleep(1)
        # Scroll details container to load data
        js_script = """
            arguments[0].scrollTo(0, 400);
        """
        driver.execute_script(js_script, elements[5])
        # Get places details
        self.details = WebDriverWait(driver, WAIT_ELEMENT_APPEAR).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, PLACE_DETAILS_SELECTOR))
        )
        details = self.details
        while True:
            if len(details[0].text) == 0 or len(details[1].text) == 0:
                time.sleep(1)
                print("Retrying to get place details...")
                self.details = driver.find_elements(By.CSS_SELECTOR, PLACE_DETAILS_SELECTOR)
                details = self.details
            else:
                break
        # Find the website and the phone number
        is_website_found = False
        is_phone_number_found = False
        for detail in self.details:
            # If the website and the phone number are found then stop searching
            if is_website_found and is_phone_number_found:
                break
            # Check if the current element is a website
            if re.match(WEBSITE_PATTERN, detail.text):
                self.website = detail.text
                is_website_found = True
            # Check if the current element is a phone number
            if re.match(PHONE_NUMBER_PATTERN, detail.text):
                self.phone_number = detail.text
                is_phone_number_found = True

    def scrape_address(self):
        return self.details[0].text

    def scrape_website(self):
        return self.website

    def scrape_phone_number(self):
        return self.phone_number
