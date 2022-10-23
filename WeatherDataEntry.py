
class WeatherDataEntry:
    def __init__(self, temperature, temperature_min, temperature_max, pressure, humidity, wind_speed, wind_angle,
                 gust_speed, time, date, weather_condition, weather_condition_detail, feels_like, dt, precip_amt):
        self.temperature = temperature
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.pressure = pressure
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.wind_angle = wind_angle
        self.gust_speed = gust_speed
        self.time = time
        self.date = date
        self.weather_condition = weather_condition
        self.weather_condition_detail = weather_condition_detail
        self.feels_like = feels_like
        self.dt = dt
        self.precip_amt = precip_amt

    def __str__(self):
        basic_string = "dt: " + str(self.dt) + "\nTemperature: " + str(self.temperature) + "\n Humidity: " + str(self.humidity) + "\n Condition: " + self.weather_condition
        return basic_string

    def get_temperature(self) -> float:
        return self.temperature

    def get_temperature_min(self) -> float:
        return self.temperature_min

    def get_temperature_max(self) -> float:
        return self.temperature_max

    def get_humidity(self) -> float:
        return self.humidity

    def get_weather_condition(self) -> str:
        return self.weather_condition

    def get_weather_condition_detail(self) -> str:
        return self.weather_condition_detail
