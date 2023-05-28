import requests
import json

def getAddress(coordinate):
    longitude = coordinate['longitude']
    latitude = coordinate['latitude']
    url = f"https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        response = response.json()
        # return response['display_name']
        address = response['address']
        return f"{address['postcode']}, {address.get('road', None)}"
