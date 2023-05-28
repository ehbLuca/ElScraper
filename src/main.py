#!./env/bin/python
import requests
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

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

def findDenyButton(driver, text):
    return driver.find_element(By.XPATH, f"//*[text()='{text}']")

def findSearchButton(driver, id):
    return driver.find_element(By.ID, id)

def findImage(driver, selector):
    return driver.find_element(By.CSS_SELECTOR, selector)

def scrapeImages(driver, skip=0):
    # Defining variables
    url = f"https://www.google.com/maps/place"
    output_file = "img_links.txt"
    # selectors
    deny_button_text = 'Alles afwijzen'
    search_button_id = 'searchbox-searchbutton'
    image_CSS = 'button[jsaction="pane.heroHeaderImage.click"] img'

    # Starting browser
    driver.implicitly_wait(0.5)
    driver.get(url)
    findDenyButton(driver, deny_button_text).click()

    # Going through the places
    places = queries.getTable('places')
    for place in places:
        print(place)
        # Create place query
        # it consists of name + address
        place_id = place[0]
        if skip > place_id:
            continue
        print(place_id)
        query = place[1] + " " + place[3]
        query = query.replace(" ", "+")

        # Search for place on maps
        driver.get(url + "/" + query)
        findSearchButton(driver, search_button_id).click()
        # Let the image load
        time.sleep(4)

        # Saving the image url
        try:
            image = findImage(driver, image_CSS)
            img_url = image.get_attribute("src")
            print(img_url)
            # write the place_id followed by the url of the image to a file seperated by a comma
            with open(output_file, "a+") as file:
                file.write(f"{place_id}, {img_url}\n")
        except:
            print("No image found.")

def main():
    driver = webdriver.Chrome()
    scrapeImages(driver)

main()
