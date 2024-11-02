import threading
import time
import mysql.connector

from constants import *
from drivermanipulator import DriverManipulator
from finder import Finder
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
        self.find_email = True
        # Instantiate finder class
        self.finder = Finder(HUNTER_API_KEYS_LIST, endpoint)
        self.manipulator = DriverManipulator("edge")
        super().__init__()

    def scrape_tab(self, places, drivermanipulator):

        # Set the end of recursive running condition
        if self.__place_index == len(self.places):
        #if self.place_index > NUMBER_ELEMENT_PER_SCROLL - 1:
            #drivermanipulator.driver.quit()
            self.__place_index = 0
            return
        # Explore places details
        self.explore_place_details(drivermanipulator, places)

    def explore_place_details(self, drivermanipulator, places):
        # Go to page URL
        place_url = places[self.__place_index]
        print("place_url: " + place_url)
        drivermanipulator.land_page_url(place_url)
        place = Place(drivermanipulator.driver)
        place_address = place.scrape_address()
        place_website = place.scrape_website()
        place_phone = place.scrape_phone_number()
        print("Place address: " + place_address)
        print("Place website: " + str(place_website))
        print("Place phone number: " + str(place_phone))

        # Save scraped data in Product table
        sql_request = """INSERT INTO googlemaps.places (
        project_name,
        place_url,
        address,
        phone,
        website) VALUES (
        %s, %s, %s, %s, %s)"""
        values = (PROJECT_NAME,
                  place_url,
                  place_address,
                  place_phone,
                  place_website)
        Model.insert_into_database(sql_request, values)

        # Find email by domain
        if self.find_email:
            self.find_email_by_domain(place_url, place_website)

        self.__place_index += 1
        # Wait between scraping places
        time.sleep(SCRAPE_PLACES_INTERVAL)
        # Increment place counter
        #self.places_counter += 1
        # Call the function recursively
        self.scrape_tab(places, drivermanipulator)

    def find_email_by_domain(self, place_url, place_website):
        # Domain website
        domain = place_website
        # Request the server
        self.finder.request_server(domain)
        # Extract contacts details
        contacts = self.finder.find_contacts()

        # Loop through the contacts list and extract email details
        is_first_email = True
        for c in contacts:
            email = str(c["value"])
            email_type = str(c["type"])
            email_confidence = str(c["confidence"])
            first_name = str(c["first_name"])
            last_name = str(c["last_name"])
            position = str(c["position"])
            seniority = str(c["seniority"])
            department = str(c["department"])
            linkedin = str(c["linkedin"])
            twitter = str(c["twitter"])
            phone_number = str(c["phone_number"])
            verification_date = str(c["verification"]["date"])
            status = str(c["verification"]["status"])

            if is_first_email:
                sql_update = """
                    UPDATE googlemaps.places
                    SET 
                        project_name = %s,
                        email = %s,
                        email_type = %s,
                        email_confidence = %s,
                        first_name = %s,
                        last_name = %s,
                        position = %s,
                        seniority = %s,
                        department = %s,
                        linkedin = %s,
                        twitter = %s,
                        phone_number = %s,
                        verification_date = %s,
                        email_status = %s
                    WHERE place_url = %s
                """

                # Define your values, including the `website` value for the WHERE clause
                values = (
                    PROJECT_NAME, email, email_type, email_confidence, first_name,
                    last_name, position, seniority, department, linkedin, twitter,
                    phone_number, verification_date, status, place_url
                )

                # Update the first entry
                Model.update_database(sql_update, values)
                is_first_email = False
            else:
                # Save email detail in the database
                # Save scraped data in Product table
                sql_request = """INSERT INTO googlemaps.places (
                                    project_name,
                                    email,
                                    email_type,
                                    email_confidence,
                                    first_name,
                                    last_name,
                                    position,
                                    seniority,
                                    department,
                                    linkedin,
                                    twitter,
                                    phone_number,
                                    verification_date,
                                    email_status) VALUES (
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (PROJECT_NAME,
                          email,
                          email_type,
                          email_confidence,
                          first_name,
                          last_name,
                          position,
                          seniority,
                          department,
                          linkedin,
                          twitter,
                          phone_number,
                          verification_date,
                          status)
                Model.insert_into_database(sql_request, values)
        # Check the remaining credits
        #finder.check_hunterio_credits()


    def scrape_places_callback(self, *args):
        self.__total_places_index += 1
        print("Deleting place details container...")
        return

    def manipulate_places_callback(self, *args):
        if not args[0]:
            return
        self.places = args[0]
        place_index = 0
        # If the index is equal to total place explored
        if self.__total_places_index >= self.total_places_explored:

            self.scrape_tab(self.places, self.manipulator)
        else:
            time.sleep(TIME_1)

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
