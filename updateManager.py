import locationManager
import weatherService
import pandas as pd


def update_all_weather():
    print("Spot 1")
    locations = locationManager.return_locations()
    print(locations)
    locations = locations.values.tolist()
    for x in locations:
        latitude = x[2]
        longitude = x[3]
        print("______________" + x[1] + "______________")
        weatherService.get_weather(latitude=latitude, longitude=longitude)
