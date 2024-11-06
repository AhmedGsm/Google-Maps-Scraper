import re

REQUEST = "real estate in Bay Area"
REQUEST0 = "real estate in Bay Area"
REQUEST1 = "Real estate in Chicago city"
REQUEST2 = "real estate in Bay Area"
REQUEST3 = "real estate in sydney"
REQUEST4 = "grossistes pharmaceutiques algerie"
REQUEST5 = "software companies in new jersey"
query = REQUEST5

PROJECT_NAME = re.sub(" ", "_", query)
BASIC_URL = "https://www.google.com/maps/search/"
URL = BASIC_URL + query
PARALLEL_BROWSER_INSTANCES_COUNT = 1
LOOP_SCRAPING_INTERVAL_TIME = 0.2
WAIT_ELEMENT_To_APPEAR = 20
WAIT_ELEMENT_APPEAR = 15
SCRAPE_PLACES_INTERVAL = 3
NO_ELEMENT_TO_SCRAPE_MESSAGE = "No element is found to scrape"

# Language
LANG = "fr"

# DEFINE TIMES CONSTANTS
TIME_1 = 1
TIME_2 = 2
TIME_3 = 3
TIME_4 = 4
TIME_5 = 5
TIME_8 = 8
TIME_10 = 10
TIME_12 = 12
TIME_15 = 15
# PARENT SCROLLABLE
PARENT_SCROLLABLE_SELECTOR = ".m6QErb.DxyBCb.kA9KIf.dS8AEf.XiKgde.ecceSd>*"
NUMBER_ELEMENT_PER_SCROLL = 5

# PLACES IN LIST
PLACE_CONTAINER_SELECTOR = ".Nv2PK.THOPZb"
"""PLACE_CONTAINER_SELECTOR_2 = ".Nv2PK.tH5CWc.THOPZb"
PLACE_CONTAINER_SELECTOR_3 = ".Nv2PK.Q2HXcd.THOPZb"""

PLACE_DETAILS_SELECTOR = ".Io6YTe.kR99db.fdkmkc"
PLACE_DETAILS_CONTAINER_SELECTOR = ".e07Vkf.kA9KIf"

# OTHER REGEX
WEBSITE_PATTERN = r"^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+(\.[a-zA-Z]{2,})+$"
PHONE_NUMBER_PATTERN = r"^\+?([0-9]{1,4}[\s-]?)+$"

# Database constants
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "0901"
MYSQL_DATABASE = "googlemaps"

# Find email from emails finders(hunter.io)
# HUNTER.IO API keys!
API_KEY_AHMED_GSM = "a32f0ffbdca8c63a0fb35db1e52a131cabc3b7c6"
API_KEY_GSM_GENIUS = "a31f0ec3e949d9f9dab2afb2c80344dffa213e19"
API_KEY_HMED_KHABER = "a663c098d8245ce32c013f1f55c99e223bf19c48"
API_KEY_AHMED_CEO_SUCCES = "33e245d3f1c8d23eed6f2b4c379053917126a19d"
API_KEY_AHMED_CEO_SUCCES_1983 = "f1f01a5d55ca2afedf7c9b39e36b593832efb639"
API_KEY_MOHAND_TAHAR = "6dde052b224d3d08b7b6cedb618bebb6d5939f5c"
API_KEY_NESRINE = "95e154b6e3b1e134c3ed3a277ed66ca2e2a53aa6"

# Hunter.io endpoint
endpoint = f"https://api.hunter.io/v2/domain-search"
HUNTER_API_KEYS_LIST = [API_KEY_AHMED_GSM,
                        #API_KEY_GSM_GENIUS,
                        #API_KEY_HMED_KHABER,
                        #API_KEY_AHMED_CEO_SUCCES,
                        #API_KEY_AHMED_CEO_SUCCES_1983,
                        #API_KEY_MOHTAHAR,
                        #API_KEY_NESRINE
]

# Snov.io api keys
SNOV_API_KEYS_LIST = [
]
"""{# AhmedGsm1983@gmail.com
'client_id': "8251531ceaa60b16053d83c06690cb20",
'client_secret': "7393e050e87c5aeb5731bbb9861e00ab"
},
{# gsmgeniu2015@gmail.com
'client_id': "5e939d2fcae4106f0e4b50fdd546e795",
'client_secret': "d609fa39f3493e1c863563c0fde4530a"
},
{# hmedkhaber@gmail.com
'client_id': "0515263d08a8721185b0733e86893838",
'client_secret': "956ce038fbb75526ae53682e2904c8c1"
},
{# ahmedceosuccess@gmail.com
'client_id': "8511689682d4b31f8dab5bc96c1893a1",
'client_secret': "51084aa1c4c457c4d9dd01d7cf09075f"
}"""
# FINDYMAIL API keys!
FINDYMAIL_API_KEY_AHMED_GSM = "NaVzLp0SOcfe6GILO5fadGv0WTtAl88woNUcbHwh6bccf8dc"