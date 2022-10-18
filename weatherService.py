import configparser

config = configparser.ConfigParser()
configFilePath = r'/Users/mike/PycharmProjects/snowHunter/settings.cfg'
config.read(configFilePath)

api_key = config['general']['apikey']


def getWeather():
    print(api_key)


# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
