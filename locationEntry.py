import WeatherDataEntry


class locationEntry:
    def __init__(self, city_name, state_name, detailed_name, latitude, longitude):
        self.city_name = city_name
        self.state_name = state_name
        self.detailed_name = detailed_name
        self.latitude = latitude
        self.longitude = longitude
        self.weather_data = []
        self.lastBeginningDtEntry = 0
        self.lastBeginningDtEntryIndex = 0
        self.entryCount = 0
        self.weather_volatile_count = 0
        self.weather_data_volatile = []

    def add_weather_entry(self, new_entry: weatherDataEntry):
        index = 0
        if new_entry.dt >= self.weather_data_volatile[0].dt:
            for x in self.weather_data:
                if x.dt == new_entry.dt:
                    x[index] = new_entry
                    break
                else:
                    index = index + 1
        else:
            self.weather_data.insert(0, new_entry)

    def volatile_to_stable(self):
        changing_element = self.weather_data_volatile[0]
        print("Changing element: " + str(changing_element))
        self.weather_data_volatile.remove(changing_element)
        self.weather_data.append(changing_element)
        print("Entry Moved")
