
from drivermanipulator import DriverManipulator
from constants import *
from wsite import Site

driver_manipulator = DriverManipulator()
googlemapssite = Site(driver_manipulator)
query = "software companies in new france"
googlemapssite.scrape_site(query)
input("Enter any key to exit!")
driver_manipulator.driver.quit()

