"""class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom


    def floor_up(self):
        if self.current < self.top:
            print(f"Moving up from {self.current} to {self.current+1}")
            self.current += 1
            return True
        else:
            return False


    def floor_down(self):
        if self.current > self.bottom:
            print(f"Moving down from {self.current} to {self.current - 1}")
            self.current -= 1
            return True
        else:
            return False

    def go_to_floor(self, floor):
        if floor > self.current:
            for n in range(floor - self.current):
                self.floor_up()
        elif floor < self.current:
            for n in range(self.current - floor):
                self.floor_down()
        else:
            print(f"We are currently on the floor {self.current}")


h = Elevator(1, 5)
target_floor = int(input("To what floor you want to go?: "))
h.go_to_floor(target_floor)
h.go_to_floor(1) #bottom

class Building:
    def __init__(self, bottom, top, elevators):
        self.elevators = []
        self.bottom = bottom
        for n in range(elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, elevator, floor):
        print(f"Moving elevator {elevator}")
        self.elevators[elevator-1].go_to_floor(floor)

    def fire_alarm(self):
        print("Fire Alarm!")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)

building = Building(1, 6, 3)

building.run_elevator(1, 5)
building.run_elevator(3, 2)
building.run_elevator(2, 4)
building.run_elevator(1, 3)


building.fire_alarm()"""


import random

class Car:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0

    def drive(self):
        self.distance += self.speed

    def __str__(self):
        return f"{self.name:15} | {self.distance:10.2f} km | {self.speed:10.2f} km/h"

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            # Generate a random change of speed for each car
            car.speed += random.uniform(-5, 5)
            car.drive()

    def print_status(self):
        print(f"{'Car Name':15} | {'Distance':10} | {'Speed':10}")
        for car in self.cars:
            print(car)

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.distance:
                return True
        return False


cars_list = []

for i in range(10):
    cars_list.append(Car("ABC-" + str(i+1), random.randint(100,200)))

grand_demolition_derby = Race("Grand Demolition Derby", 8000, cars_list)

hour = 1
while not grand_demolition_derby.race_finished():
    grand_demolition_derby.hour_passes()
    if hour % 10 == 0:
        print(f"\nRace status after {hour} hours:")
        grand_demolition_derby.print_status()
    hour += 1

print("\nRace finished! Final status:")
grand_demolition_derby.print_status()










