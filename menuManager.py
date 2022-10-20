import locationManager
import updateManager


# Basic functionality for a simple terminal menu


def menu_main():
    print("---SnowHunter by Michael Bailey---")
    print("1. Review forecasts")
    print("2. Review locations")
    print("3. Add new location")
    print("4. Exit Program")
    selection = int(input("Please enter the number of the action you would like to perform: "))

    if selection == 1:
        forecast_menu()
        menu_main()
    elif selection == 2:
        print(locationManager.return_locations())
        menu_main()
    elif selection == 3:
        add_new_location()
        menu_main()
    elif selection == 4:
        exit()
    # if input("Would you like to review location forecasts? Y/N: ") == "Y":
    #     forecast_menu()
    #     menu_main()
    # elif input("Would you like to review current locations? Y/N: ") == "Y":
    #     print(locationManager.return_locations())
    #     menu_main()
    # elif input("Would you like to add a new location? Y/N: ") == "Y":
    #     add_new_location()
    #     menu_main()
    # else:
    #     if input("Would you like to exit? Y/N: ") == "Y":
    #         exit()
    #     else:
    #         menu_main()


def add_new_location():
    detail_name = input("Enter detailed name: ")
    actual_name = input("Enter actual name: ")
    longitude = input("Enter Longitude: ")
    latitude = input("Enter Latitude: ")
    locationManager.write_location(detail_name=detail_name, actual_name=actual_name, long=longitude, lat=latitude)
    if input("New location has been added, would you like to add another? Y/N: ") == 'Y':
        add_new_location()


def review_locations_menu():
    choice = input("Would you like to edit, add or remove a location?: ")
    if choice == "edit":
        edit_locations()
    elif choice == "add":
        add_new_location()
    elif choice == "remove":
        remove_location()
    else:
        print("Please enter a valid option")
        review_locations_menu()


def edit_locations():
    entryToEdit = locationManager.get_specific_entry(int(input("Enter number of location to edit: ")))
    print(entryToEdit)


def remove_location():
    print("empty")


def forecast_menu():
    print("---Forcast Update Menu---")
    print("1. See latest forcast for all locations")
    print("2. See latest forecast for specific location")
    print("3. Return to menu")
    selection = int(input("Please enter the number of the action you would like to perform: "))

    if selection == 1:
        updateManager.update_all_weather()
    elif selection == 2:
        print(locationManager.return_locations())
        updateManager.update_specific_location(int(input("Enter the number of the location to review")))
    elif selection == 3:
        menu_main()
    else:
        print("Please select a valid option")
        forecast_menu()