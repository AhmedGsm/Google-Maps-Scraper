import threading
import time

from constants import *
from drivermanipulator import DriverManipulator
from model import Model
from place import Place
from scrollable import Scrollable


class Site(Scrollable):
    def __init__(self, driver_manipulator):
        self.driver_manipulator = driver_manipulator
        self.parent_scrollable = None
        self.__place_index = 0
        self.__total_places_index = 0
        self.total_places_explored = 0
        super().__init__()

    def scrape_tab(self, places, drivermanipulator):

        # Set the end of recursive running condition
        if self.__place_index == len(self.places):
        #if self.place_index > NUMBER_ELEMENT_PER_SCROLL - 1:
            drivermanipulator.driver.quit()
            self.__place_index = 0
            return
        # Explore places details
        self.explore_place_details(drivermanipulator, places)

    def explore_place_details(self, drivermanipulator, places):
        # Go to page URL
        url = places[self.__place_index]
        drivermanipulator.land_page_url(url)
        place = Place(drivermanipulator.driver)
        place_address = place.scrape_address()
        place_website = place.scrape_website()
        place_phone = place.scrape_phone_number()
        print("Place address: " + place_address)
        print("Place website: " + place_website)
        print("Place phone number: " + place_phone)
        # Save scraped data in Product table
        sql_request = """INSERT INTO googlemaps.places (
        project_name,
        url,
        address,
        phone,
        website) VALUES (
        %s, %s, %s, %s, %s)"""
        values = (PROJECT_NAME,
                  url,
                  place_address,
                  place_phone,
                  place_website)
        Model.insert_into_database(sql_request, values)
        self.__place_index += 1
        # Wait between scraping places
        time.sleep(SCRAPE_PLACES_INTERVAL)
        # Increment place counter
        #self.places_counter += 1
        # Call the function recursively
        self.scrape_tab(places, drivermanipulator)

    def scrape_places_callback(self, *args):
        self.__total_places_index += 1
        print("Deleting place details container...")
        return

    def manipulate_places_callback(self, *args):
        self.places = args[0]
        place_index = 0
        # If the index is equal to total place explored
        if self.__total_places_index >= self.total_places_explored:
            self.scrape_tab(self.places, DriverManipulator("edge"))
        else:
            time.sleep(TIME_10)

        # Increment current counter
        #self.index += 1

        #thread = threading.Thread(target=self.scrape_tab, args=(self.places, DriverManipulator("firefox")))
        #thread.start()
        print("self.__place_index " + str(self.__place_index))
        """for i in range(0, PARALLEL_BROWSER_INSTANCES_COUNT):
            #thread = threading.Thread(target=self.scrape_tab, args=(args[0][place_index], DriverManipulator("firefox")))
            #thread.start()
            self.scrape_tab(self.places[self.place_index], DriverManipulator("firefox"))
            self.place_index += 1"""
        #print("scrape_places_callback")
        return

    def scrape_places(self,):
        self.scroll_and_callback(self.driver_manipulator.driver, PARENT_SCROLLABLE_SELECTOR, PLACE_CONTAINER_SELECTOR, LOOP_SCRAPING_INTERVAL_TIME,
                                   self.scrape_places_callback, self.manipulate_places_callback,
                                   end_message="Scraping finished!")

    def scrape_site(self):
        self.driver_manipulator.land_page_url(URL)
        #self.parent_scrollable = self.driver_manipulator.driver.find_element(By.CSS_SELECTOR, PARENT_SCROLLABLE_SELECTOR)
        # places = self.driver.find_elements(By.CSS_SELECTOR, PLACE_CONTAINER_SELECTOR)
        self.scrape_places()
        #self.driver.quit()
