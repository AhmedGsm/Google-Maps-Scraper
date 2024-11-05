import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import *

class Place:
    def __init__(self, driver):
        self.driver = driver
        self.website = None
        self.phone_number = None
        self.initializations(driver)

    def initializations(self, driver):
        # Find elements to pick 6th element that contains places details
        elements = driver.find_elements(By.CSS_SELECTOR, PLACE_DETAILS_CONTAINER_SELECTOR)

        # Scroll details container to load data
        js_script = """
            elements = document.querySelectorAll(arguments[0])
            for (let e of elements) {
                if (e.scrollHeight > 400) {
                    e.scrollTo(0, 400);
                }
                console.log(e.scrollHeight)
            }
        """
        driver.execute_script(js_script, PLACE_DETAILS_CONTAINER_SELECTOR)
        # Get places details
        while True:
            self.details = WebDriverWait(driver, WAIT_ELEMENT_APPEAR).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, PLACE_DETAILS_SELECTOR))
            )

            if not self.details:
                print("Retrying to get place details...")
                time.sleep(2)
            else:
                break
        # Find the website and the phone number
        """is_website_found = False
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
                is_phone_number_found = True"""

    def scrape_address(self):
        # Find the <div> element containing the phone number by first locating the span with ''
        try:
            return self.driver.find_element(
                By.XPATH,
                "//span[contains(text(), '')]/ancestor::div[contains(@class, 'AeaXub')]//div[contains(@class, 'Io6YTe')]"
            ).text
        except:
            return None

    def scrape_website(self):
        # Find the <div> element containing the phone number by first locating the span with ''
        try:
            return self.driver.find_element(
                By.XPATH,
                "//span[contains(text(), '')]/ancestor::div[contains(@class, 'AeaXub')]//div[contains(@class, 'Io6YTe')]"
            ).text
        except:
            return None

    def scrape_phone_number(self):
        # Find the <div> element containing the phone number by first locating the span with ''
        try:
            return self.driver.find_element(
                By.XPATH,
                "//span[contains(text(), '')]/ancestor::div[contains(@class, 'AeaXub')]//div[contains(@class, 'Io6YTe')]"
            ).text
        except:
            return None
