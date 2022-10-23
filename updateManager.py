import locationManager
import weatherService
import pandas as pd
import dataDisplay
from WeatherDataEntry import WeatherDataEntry

def update_all_weather():
    print("Spot 1")
    locations = locationManager.return_locations()
    print(locations)
    locations = locations.values.tolist()
    for x in locations:
        latitude = x[2]
        longitude = x[3]
        print("______________" + x[1] + "______________")
        dataDisplay.data_text_display(weatherService.get_weather(latitude=latitude, longitude=longitude))


def update_specific_location(index: int):
    locations = locationManager.return_locations()
    locations = locations.values.tolist()
    latitude = locations[index][2]
    longitude = locations[index][3]
    print("______________" + locations[index][1] + "______________")
    weather = weatherService.get_weather(weatherService.get_weather(latitude=latitude, longitude=longitude))

    dataDisplay.data_text_display(weather)


def store_weather_data(data: []):
    print("Hello")


def pull_temp_data(data: []):
    new_temp_data = []
    for x in data['list']:
        new_temp_data.append(float(x['main']['temp']))
    print(new_temp_data)


def test():
    test_entry = WeatherDataEntry(temperature=99, temperature_min= 88, temperature_max= 104, humidity= 67, wind_speed= 3.2, wind_angle= 270, gust_speed= 5, pressure= 1000, time='3:00 PM', date='10/21/2022', dt=1666386000, weather_condition="Cloudy", weather_condition_detail="partly cloudy", feels_like=32, precip_amt=0)
    print(test_entry)