# TODO Add .csv read/write functionality
# TODO Add conversion from location name to lat/long
# TODO Add return of list of stored locations
import pandas as pd
from os.path import exists

location_file = '/Users/mike/PycharmProjects/snowHunter/locations.csv'

location_header = ['Detailed Name', 'Actual Name', 'latitude', 'longitude']


# def newLocation (lat, long):
#

# Function to return a list of locations with names, latitudes, longitudes


# def returnLoocations():
#
#
# def readLocation():
#
#TODO Change to pandas.concat instead of append
def write_location(detail_name: str, actual_name: str, long: float, lat: float) -> pd.DataFrame:
    # Checks if locations.csv exists, if not sets it up with proper headers
    if exists(location_file):
        data = pd.read_csv(filepath_or_buffer=location_file, header= 0)
        print("Found file")
        print(data)
    else:
        data = pd.DataFrame(columns=location_header)

    # takes function inputs and puts them in the appropriate format
    data_entry = [[detail_name, actual_name, long, lat]]
    # Puts new data in proper data frame format
    added_data = pd.DataFrame(columns=location_header, data=data_entry)
    # Appends data to existing data
    data = data.append(other=added_data, ignore_index=False)
    print(data)
    # Returns data to CSV file
    data.to_csv(path_or_buf=location_file,index=False)
    return data
