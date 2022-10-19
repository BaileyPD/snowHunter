import locationManager

# Basic functionality for a simple terminal menu


def menu_main():
    # print("Would you like to review location forecasts? Y/N")
    if input("Would you like to review location forecasts? Y/N: ") == "Y":
        try:
            print(locationManager.return_locations())
        except:
            if input("There are no locations saved. Would you like to add one? Y/N: ") == 'Y':
                add_new_location()
        menu_main()
    else:
        if input("Would you like to review current locations? Y/N: ") == "Y":
            print(locationManager.return_locations())
            menu_main()
        else:
            if input("Would you like to add a new location? Y/N: ") == "Y":
                add_new_location()
                menu_main()


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
        print("Plese enter a valid option")
        review_locations_menu()


def edit_locations():
    entryToEdit = locationManager.get_specific_entry(int(input("Enter number of location to edit: ")))
    print(entryToEdit)


def remove_location():
    print("empty")
