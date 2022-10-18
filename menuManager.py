import locationManager

# Basic functionality for a simple terminal menu


def menu_main():
    # print("Would you like to review location forecasts? Y/N")
    if input("Would you like to review location forecasts? Y/N:") == "Y":
        print(locationManager.return_locations())
        menu_main()
    else:
        # print("Would you like to review current locations? Y/N")
        if input("Would you like to review current locations? Y/N") == "Y":
            print(locationManager.return_locations())
            menu_main()
        else:
            print("Would you like to add a new location? Y/N")
            if input() == "Y":
                print("Enter detailed name")
                detail_name = input()
                print("Enter actual name")
                actual_name = input()
                print("Enter Longitude")
                longitude = input()
                print("Enter Latitude")
                latitude = input()
                locationManager.write_location(detail_name=detail_name, actual_name=actual_name, long= longitude, lat=latitude)
                print("New location has been added")
                menu_main()