#Import libraries
import webbrowser
import folium
import phonenumbers
from phonenumbers import geocoder
from opencage.geocoder import OpenCageGeocode

#Define contants
KEY = '2ec6f6cd54094fe9be5134c0f0652f08'

#Define functions
def get_coordinates(number):
    phoneNumber = phonenumbers.parse(number, None)
    loc = geocoder.description_for_number(phoneNumber, 'en')
    geoCoder = OpenCageGeocode('2ec6f6cd54094fe9be5134c0f0652f08')
    query = str(loc)
    location = geoCoder.geocode(query)
    print(phoneNumber, number)
    latitude = location[0]['geometry']['lat']
    longitude = location[0]['geometry']['lng']
    coordinates = [latitude, longitude]
    return coordinates, loc
    
def map_coordinates(coordinates, loc):
    map = folium.Map(location=coordinates, zoom_start=3)
    folium.Marker(coordinates, popup=loc).add_to((map))
    map.save(r"website\templates\location.html")

def open_map_file():
    webbrowser.open_new_tab(r"templates\location.html")
