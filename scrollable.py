import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from constants import WAIT_ELEMENT_To_APPEAR


class Scrollable:
    def __init__(self):
        #self.is_element_found = False
        pass

    def scroll_and_callback(self, driver, parent_scrollable, children_selector, load_time, loop_callback, end_message, delete_element=True):
        while True:
            try:
                # Try to retrieve the first liker div if exist(before it will deleted)
                first_child = WebDriverWait(driver, WAIT_ELEMENT_To_APPEAR).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, children_selector))
                )
                print("1-The height of the child element is: " + str(first_child.size["height"]))

                #div_height = driver.execute_script("return window.getComputedStyle(arguments[0]).height;", first_child)
                print("2-The height of the parent element is: " + str(parent_scrollable.size["height"]))
                #self.is_element_found = True
            except:
                #if self.is_element_found:
                #    print(end_message)
                #else:
                print("No element is found to scrape")

                break
            # Run callback function every cycle of the loop
            loop_callback(first_child)
            # Run js script to remove the first child from the DOM
            if delete_element:
                self.delete_js_dom_element(driver, children_selector)
            # Pause program to prevent excessive server requests to prevent website penalties
            time.sleep(load_time)

    def delete_js_dom_element(self, driver, children_selector):
        script = f""" 
                     likersDivs = document.querySelector('{children_selector}')
                     likersDivs.remove()
            """
        driver.execute_script(script)