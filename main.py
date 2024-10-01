
from driver import Driver
from constants import *

browser_driver = Driver(browser='firefox')
browser_driver.land_page_url(URL)
input("Press any key to exit!")
browser_driver.quit()
