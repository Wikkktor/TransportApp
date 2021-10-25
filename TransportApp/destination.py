import requests
from passwords import API_KEY


def get_distance_time_values(origin, destination):
    url = f"""https://maps.googleapis.com/maps/api/distancematrix/json?origins=
                {origin}&destinations={destination}&mode=DRIVING&language=pl-PL&key={API_KEY}"""
    r = requests.get(url).json()
    time_distance = []
    for obj in r['rows']:
        for data in obj['elements']:
            time_distance.append(data['distance']['text'])
            time_distance.append(data['duration']['text'])
    return time_distance
