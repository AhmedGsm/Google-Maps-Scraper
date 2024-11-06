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

    def scrape_name(self):
        place_name_raw = self.driver.find_element(By.CSS_SELECTOR, ".DUwDvf.lfPIob").get_attribute("outerHTML")
        return re.search("<.*?/.*?>(.*?)<.*?/.*?>", place_name_raw, re.DOTALL).group(1).strip()

    def scrape_address(self):
        i = 0
        retrying_time = 3600# Retry in 1 hours until the browser is active(not in the background or minimized!)
        # Find the <div> element containing the phone number by first locating the span with ''
        try:
            while True:
                address = self.driver.find_element(
                    By.XPATH,
                    "//span[contains(text(), '')]/ancestor::div[contains(@class, 'AeaXub')]//div[contains(@class, 'Io6YTe')]"
                ).text
                if address:
                    return address
                elif i == retrying_time:
                    return None
                i += 1
                print("Retrying to scrape place address...")
                time.sleep(1)
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
