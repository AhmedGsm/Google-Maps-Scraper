import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from constants import *
from model import Model


class Scrollable:
    def __init__(self):
        self.is_element_found = False
        self.scrape_index = 0
        pass

    def scroll_and_callback(self, driver, parent_selector, children_selector, load_time,
                            loop_callback, bulk_callback, end_message="", delete_element=True):
        while True:
            try:
                # Try to retrieve the first liker div if exist(before it will deleted)
                WebDriverWait(driver, TIME_5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, PLACE_CONTAINER_SELECTOR))
                )
                self.is_element_found = True
            except:
                if self.is_element_found:
                    print(end_message)
                else:
                    print(NO_ELEMENT_TO_SCRAPE_MESSAGE)
                break
            # Initialize link elements list
            all_link_elements = []

            # Scroll the div using JavaScript
            js_script = f"""
            var parentElement = document.querySelector("{parent_selector}");
            preScrollTop = parentElement.scrollTop
            parentElement.scrollTo(0, preScrollTop + 150);
            if (preScrollTop == parentElement.scrollTop) {{
                return true;
            }} else {{
                return false;
            }}
            """

            while len(all_link_elements) < NUMBER_ELEMENT_PER_SCROLL * 2:
                end_of_scrolling = driver.execute_script(js_script)
                if end_of_scrolling:
                    print("Container arrives to end of scrolling!")
                    break
                # Manipulate places list and empty it after finishing
                # Get the link of element
                all_link_elements = driver.find_elements(By.CSS_SELECTOR, children_selector)
                time.sleep(1)
            link_elements = all_link_elements[0: NUMBER_ELEMENT_PER_SCROLL]
            places_links = []
            for l in link_elements:
                place_url = l.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                entries = Model.read_from_database(f"SELECT website FROM googlemaps.places WHERE place_url = '{place_url}' ")
                # If the place is saved in the database do not add it to the list
                # to prevent re-explore it!
                if not entries:
                    places_links.append(place_url)

            # Run conditional callback function to treat place list
            bulk_callback(places_links)

            # Delete place elements from the DOM to prevent overloading the memory
            if delete_element:
                for i in range(NUMBER_ELEMENT_PER_SCROLL):
                    self.delete_js_dom_element(driver, children_selector)
                    loop_callback()
                    time.sleep(LOOP_SCRAPING_INTERVAL_TIME)

    def delete_js_dom_element(self, driver, children_selector):
        script = f""" 
                     likersDivs = document.querySelector('{children_selector}')
                     likersDivs.remove()
            """
        driver.execute_script(script)