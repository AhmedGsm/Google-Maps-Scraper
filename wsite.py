import re
import threading
import time
import mysql.connector

from constants import *
from drivermanipulator import DriverManipulator
from finder import Finder
from snovio_finder import SnovioFinder
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
        # No not assign this value, because it will update from the callback function in scrollable.py
        self.update_entries = None
        # Instantiate finder class
        self.hunter_finder = Finder(HUNTER_API_KEYS_LIST, endpoint)
        self.snov_finder = SnovioFinder(SNOV_API_KEYS_LIST)
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
        # Change language of URL
        place_url = re.sub(r"&hl=fr", f"&hl={LANG}", place_url)
        print("place_url: " + place_url)
        drivermanipulator.land_page_url(place_url)
        place = Place(drivermanipulator.driver)
        self.short_url = place_url.split("/data=!")[0]
        place_address = place.scrape_address()
        place_website = place.scrape_website()
        place_phone = place.scrape_phone_number()
        print("Short URL: " + self.short_url)
        print("Place address: " + str(place_address))
        print("Place website: " + str(place_website))
        print("Place phone number: " + str(place_phone))

        # Save scraped data in Product table
        sql_request = """INSERT INTO googlemaps.places (
        project_name,
        place_url,
        short_url,
        address,
        phone,
        website) VALUES (
        %s, %s, %s, %s, %s, %s)"""
        values = (PROJECT_NAME,
                  place_url,
                  self.short_url,
                  place_address,
                  place_phone,
                  place_website)

        # Convert insert to update request if the entry is exists in the database
        update_request = ""
        if self.update_entries:
            update_request = f"""UPDATE googlemaps.places SET
            project_name = %s,
            address = %s,
            phone = %s,
            website = %s 
            WHERE place_url = %s """
            update_values = (PROJECT_NAME, place_address, place_phone, place_website, place_url)
            Model.insert_into_database(sql_request, values, True, update_request, update_values)
        else:
            Model.insert_into_database(sql_request, values)


        # Find email by domain
        if self.find_email:
            contacts = self.hunter_finder.find_email_by_domain(place_website)
            if not contacts:
                # Create snov.io email finder object
                print("Switching to snov.io email finder")
                contacts = self.snov_finder.get_domain_search(place_website)
                if contacts:
                    contacts = self.format_contacts_from_snovio_to_hunterio(contacts["data"])

            # Save email details in the database
            self.save_email_details_in_database(contacts, values)

        self.__place_index += 1
        # Wait between scraping places
        time.sleep(SCRAPE_PLACES_INTERVAL)
        # Increment place counter
        #self.places_counter += 1
        # Call the function recursively
        self.scrape_tab(places, drivermanipulator)

    def save_email_details_in_database(self, contacts, values):
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
                    WHERE place_url = %s """


                # Define your values, including the `website` value for the WHERE clause
                values = (
                    PROJECT_NAME, email, email_type, email_confidence, first_name,
                    last_name, position, seniority, department, linkedin, twitter,
                    phone_number, verification_date, status, values[1]
                )

                # Update the first entry
                Model.update_database(sql_update, values)
                is_first_email = False
            else:
                # Save email detail in the database
                # Save scraped data in Product table
                sql_request = """INSERT INTO googlemaps.places (
                                    project_name,
                                    place_url,
                                    address,
                                    phone,
                                    website
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
                                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                values = (PROJECT_NAME,
                          values[1],
                          values[3],
                          values[4],
                          values[5],
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
                # Insert entries or update if they are already exist
                Model.insert_into_database(sql_request, values)

    def format_contacts_from_snovio_to_hunterio(self, data):
        formatted_contacts = []
        for i in range(len(data)):
            # Initial contact object
            contact = {}
            contact["verification"] = {}
            # Assign and format snovio contact details
            contact["value"] = data[i]["email"]
            contact["type"] = data[i]["type"]
            contact["verification"]["status"] = data[i]["status"]
            try:
                contact["first_name"] = data[i]["first_name"]
                contact["last_name"] = data[i]["last_name"]
                contact["position"] = data[i]["position"]
                contact["linkedin"] = data[i]["sourcePage"]
            except:
                contact["first_name"] = "N/A"
                contact["last_name"] = "N/A"
                contact["position"] = "N/A"
                contact["linkedin"] = "N/A"
            contact["confidence"] = "N/A"
            contact["seniority"] = "N/A"
            contact["department"] = "N/A"
            contact["twitter"] = "N/A"
            contact["phone_number"] = "N/A"
            contact["verification"]["date"] = "N/A"
            formatted_contacts.append(contact)
        return formatted_contacts

    def scrape_places_callback(self, *args):
        self.__total_places_index += 1
        print("Deleting place details container...")
        return

    def manipulate_places_callback(self, *args):
        # Check if update entries is activated from the callback function!
        self.update_entries = args[1]

        # If places list is empty then quit
        if not args[0]:
            return
        self.places = args[0]

        # If the index is equal to total place explored
        if self.__total_places_index >= self.total_places_explored:

            self.scrape_tab(self.places, self.manipulator)
        else:
            time.sleep(TIME_8)

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
