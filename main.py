# The file where allowed vehicles are stored
VEHICLES_FILE = "allowed_vehicles.txt"

# Function to initialize the file with default vehicles if it doesn't exist
def initialize_file():
    default_vehicles = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Rivian R1T', 'Ram 1500']
    try:
        with open(VEHICLES_FILE, 'x') as f:
            f.write("\n".join(default_vehicles))
    except FileExistsError:
        pass 

# Function to load vehicles from the file
def load_vehicles():
    with open(VEHICLES_FILE, 'r') as f:
        return [line.strip() for line in f.readlines()]

# Function to save vehicles to the file
def save_vehicles(vehicles):
    with open(VEHICLES_FILE, 'w') as f:
        f.write("\n".join(vehicles))
    print(" ")

# Function to print all allowed vehicles
def print_allowed_vehicles():
    print(" ")
    vehicles = load_vehicles()
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in vehicles:
        print(f"- {vehicle}")
    print(" ")

# Function to search for a specific vehicle
def search_vehicle():
    print(" ")
    print("********************************")
    print("Please Enter the full Vehicle name:")
    vehicle_name = input("           ").strip()
    vehicles = load_vehicles()
    if vehicle_name in vehicles:
        print(" ")
        print(f"{vehicle_name} is an authorized vehicle.")
    else:
        print(" ")
        print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again.")
    print("********************************")
    print(" ")

# Function to add a new vehicle
def add_vehicle():
    print(" ")
    print("********************************")
    print("Please Enter the full Vehicle name you would like to add:")
    new_vehicle = input("           ").strip()
    vehicles = load_vehicles()
    if new_vehicle not in vehicles:
        vehicles.append(new_vehicle)
        save_vehicles(vehicles)
        print(f'You have added "{new_vehicle}" as an authorized vehicle.')
    else:
        print(" ")
        print(f'"{new_vehicle}" is already in the list of authorized vehicles.')
    print("********************************")
    print(" ")

# Function to delete a vehicle
def delete_vehicle():
    print(" ")
    print("********************************")
    print("Please Enter the full Vehicle name you would like to REMOVE:")
    vehicle_to_delete = input("           ").strip()
    vehicles = load_vehicles()
    if vehicle_to_delete in vehicles:
        print(" ")
        print(f'Are you sure you want to remove "{vehicle_to_delete}" from the Authorized Vehicles List?')
        confirmation = input('Type "yes" to confirm: ').strip().lower()
        if confirmation == 'yes':
            vehicles.remove(vehicle_to_delete)
            save_vehicles(vehicles)
            print(f'You have REMOVED "{vehicle_to_delete}" as an authorized vehicle.')
        else:
            print(" ")
            print("No changes were made to the Authorized Vehicles List.")
    else:
        print(" ")
        print(f'"{vehicle_to_delete}" is not in the list of authorized vehicles.')
    print("********************************")
    print(" ")

# Function to handle menu events
def handle_menu_choice(choice):
    if choice == '1':
        print_allowed_vehicles()
    elif choice == '2':
        search_vehicle()
    elif choice == '3':
        add_vehicle()
    elif choice == '4':
        delete_vehicle()
    elif choice == '5':
        print(" ")
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        return False  # Exits the menu loop
    else:
        print("Invalid choice. Please try again.")
    return True  # Keeps the menu loop running

# Main menu function
def menu():
    initialize_file()  # Ensure the file is initialized before showing the menu
    running = True
    while running:
        print("********************************")
        print("AutoCountry Vehicle Finder v0.5")
        print("********************************")
        print(" ")
        print("Please Enter the following number below from the following menu:")
        print(" ")
        print("1. PRINT all Authorized Vehicles")
        print("2. SEARCH for Authorized Vehicles")
        print("3. ADD Authorized Vehicle")
        print("4. DELETE Authorized Vehicle")
        print("5. Exit")
        print("********************************")

        choice = input("           ")
        running = handle_menu_choice(choice)

# Run the program
if __name__ == "__main__":
    menu()
