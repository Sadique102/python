"""class Publication:
    def __init__(self, name):
        self.name = name

    def print_information(self):
        print(f"Name: {self.name}")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        super().__init__(name)
        self.chief_editor = chief_editor

    def print_information(self):
        super().print_information()
        print(f"Chief Editor: {self.chief_editor}")


# Creating instances
donald_duck = Magazine("Donald Duck", "Aki Hyyppä")
compartment_no_6 = Book("Compartment No. 6", "Rosa Liksom", 192)

# Printing information
donald_duck.print_information()
print("\n")
compartment_no_6.print_information()"""


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.kilometers_driven = 0

    def drive(self, hours):
        self.kilometers_driven += self.max_speed * hours

    def get_kilometers(self):
        return self.kilometers_driven


class ElectricCar(Car):
    def __init__(self, registration_number, max_speed, battery_capacity):
        super().__init__(registration_number, max_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, max_speed, tank_volume):
        super().__init__(registration_number, max_speed)
        self.tank_volume = tank_volume


# Creating instances
electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)

# Selecting speeds for both cars and making them drive for three hours
electric_car.drive(3)
gasoline_car.drive(3)

# Printing out the values of their kilometer counters
print(f"Electric Car Kilometers: {electric_car.get_kilometers()} km")
print(f"Gasoline Car Kilometers: {gasoline_car.get_kilometers()} km")




