import configparser

configParser = configparser.ConfigParser()
configFilePath = r'/Users/mike/PycharmProjects/snowHunter/config.txt'
configParser.read(configFilePath)

api_key = configParser('Key Section', 'api_key')


def getWeather():
    print(api_key)


# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
