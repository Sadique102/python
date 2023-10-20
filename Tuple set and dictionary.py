#1
"""seasons = ("Winter", "Spring","Summer", "Autumn")
month_number = int(input("Enter a month number (1-12): "))

if month_number < 1 or month_number > 12:
    print("Invalid month number, Please enter a number between 1 and 12.")
else:
    season_index = (month_number % 12) // 3
    print(f"The season for month is {seasons[season_index]}.")"""


#2
"""names_set = set()

while True:
    name = input("Enter a name (or press Enter to finish): ")
    if name == "":
        break


    if name in names_set:
        print("Existing name")
    else:
        print("New name")
        names_set.add(name)
print("\nList of input names:")
for name in names_set:
    print(name)"""



#3
"""airport_data = {}



def add_airport():
    icao_code = input("Enter the ICAO code of the airport: ").strip().upper()
    airport_name = input("Enter the name of the airport: ")
    airport_data[icao_code] = airport_name
    print(f"Airport {icao_code} ({airport_name}) has been added to the database.")


def fetch_airport():
    icao_code = input("Enter the ICAO code of the airport you want to fetch: ").strip().upper()
    if icao_code in airport_data:
        print(f"The name of the airport with ICAO code {icao_code} is {airport_data[icao_code]}.")
    else:
        print(f"Airport with ICAO code {icao_code} not found in the database.")


while True:
    print("\nAirport Database")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_airport()
    elif choice == "2":
        fetch_airport()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")"""


