
from drivermanipulator import DriverManipulator
from constants import *
from wsite import Site

driver_manipulator = DriverManipulator()
googlemapssite = Site(driver_manipulator)
googlemapssite.scrape_site()
input("Enter any key to exit!")
driver_manipulator.driver.quit()

