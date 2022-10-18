import configparser
import requests
#import JSON

config = configparser.ConfigParser()
configFilePath = r'/Users/mike/PycharmProjects/snowHunter/settings.cfg'
config.read(configFilePath)

api_key = config['general']['apikey']

Base_URL = 'http://api.openweathermap.org/data/2.5/forecast'


def get_weather(latitude: float, longitude: float):
    print(api_key)
    URL = '?lat={' + str(latitude) + "}&lon={" + str(longitude) + "}&appid={" + api_key + "}"
    print(URL)
    combined_url = Base_URL + URL
    print(combined_url)
    response = requests.get(combined_url)
    print(response)
    if response.status_code == 200:
        data = response.json()
        main = data['Main']
        print(main)

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
