import threading
from constants import *
from drivermanipulator import DriverManipulator
from selenium.webdriver.common.by import By
from scrollable import Scrollable


class Site(Scrollable):
    def __init__(self, driver_manipulator):
        self.driver_manipulator = driver_manipulator
        self.parent_scrollable = None

    def scrape_tab(self):
        pass


    def scrape_places_callback(self,parent):
        print("scrape_places_callback")
        pass

    def scrape_places(self,):
        self.scroll_and_callback(self.driver_manipulator.driver, self.parent_scrollable, PLACE_CONTAINER_SELECTOR, LOOP_SCRAPING_INTERVAL_TIME,
                                   self.scrape_places_callback,
                                   "Scraping finished!")

    def scrape_site(self):
        self.driver_manipulator.land_page_url(URL)
        self.parent_scrollable = self.driver_manipulator.driver.find_element(By.CSS_SELECTOR, PARENT_SCROLLABLE_SELECTOR)
        # places = self.driver.find_elements(By.CSS_SELECTOR, PLACE_CONTAINER_SELECTOR)
        self.scrape_places()
        #self.driver.quit()
