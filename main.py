#!./env/bin/python
import requests
import time

from selenium import webdriver

import gmrequests
import queries

def setAddresses():
    places = queries.getTable('places')
    for place in places:
        print(place)
        coordinate = place[2].split(' ')
        address = gmrequests.getAddress({
            'latitude': coordinate[0],
            'longitude': coordinate[1]
            })
        place_id = place[0]
        queries.updateAddress(place_id=place_id, address=address)

def main():
    queries.getTable('places')
    # driver = webdriver.Chrome()
    # driver.get(URL)
    # driver.quit()

main()
