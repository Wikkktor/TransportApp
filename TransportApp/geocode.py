from geopy.exc import GeocoderUnavailable
from geopy.geocoders import Nominatim


def get_location_geo(adress):
    lst = []
    locator = Nominatim(user_agent="Project App")
    location = locator.geocode(adress)
    lst.append(location.latitude)
    lst.append(location.longitude)
    try:
        return lst
    except GeocoderUnavailable:
        return lst



