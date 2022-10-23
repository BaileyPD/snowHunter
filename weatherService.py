import configparser
import requests
#import JSON

config = configparser.ConfigParser()
configFilePath = r'/Users/mike/PycharmProjects/snowHunter/settings.cfg'
config.read(configFilePath)

api_key = config['general']['apikey']

Base_URL = 'https://api.openweathermap.org/data/2.5/forecast'


def get_weather(latitude: float, longitude: float) -> []:
    URL = '?lat=' + str(latitude) + "&lon=" + str(longitude) + "&appid=" + api_key + "&units=imperial"
    combined_url = Base_URL + URL
    response = requests.get(combined_url)
    print("Full Response: " + str(response))
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data
        # print(data)
        # data_list = data['list']
        # for x in data_list:
        #     print("Temperature: " + str(x['main']['temp']) + "F at " + str(x['main']['humidity']) + " percent humidity" )
        #     print(x['weather'])
        #print(main)

# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
