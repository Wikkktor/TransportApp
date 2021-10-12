from geopy.geocoders import Nominatim


def get_location_geo(adress):
    locator = Nominatim(user_agent="Project App")
    location = locator.geocode(adress)
    return [location.latitude, location.longitude]


print(get_location_geo("Pruszkowska 35, Nadarzyn 05-830"))

