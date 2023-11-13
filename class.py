#1
"""class Car:

    def __init__(self, registrationN, maximumS):
        self.registrationN = registrationN
        self.maximumS = maximumS
        self.currentS = 0
        self.travelledD = 0


my_car = Car("ABC-123", 142)

print("Registration Number:", my_car.registrationN)
print("Maximum Speed:", my_car.maximumS, "km/h")
print("Current Speed:", my_car.currentS, "km/h")
print("Travelled Distance:", my_car.travelledD, "km")"""


#2 && 3
"""class Car:
    def __init__(self, regisN, maxS):
        self.regisN = regisN
        self.maxS = maxS
        self.speed = 0
        self.travelledD = 0


    def accelerate(self, acceleration):
        self.speed = min(max(self.speed+acceleration, 0), self.maxS)


    def  drive(self, time):
        self.travelledD +=  self.speed * time


tesla = Car("ABC-123", 143)
print("", tesla.regisN)

tesla.accelerate(30)
tesla.accelerate(50)
tesla.accelerate(70)

print("", tesla.speed)

tesla.accelerate(-200)
print("", tesla.speed)

tesla.accelerate(60)
print("", tesla.speed)
tesla.drive(1.5)
print("",  tesla.travelledD)"""


#4

"""import random

class Car:
    def __init__(self, registration, maxSpeed):
        self.registration = registration
        self.maxSpeed = maxSpeed
        self.speed = 0
        self.odometer = 0


    def accelerate(self, acceleration):
        self.speed = min(max(self.speed+acceleration, 0), self.maxSpeed)

    def drive(self, time):
        self.odometer += self.speed * time


cars = []

for i in range(10):
    cars.append(Car("ABC-" + str(i+1), random.randint(100,200)))


odomax = 0
while odomax < 10000:
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1.)
        odomax = max(car.odometer, odomax)

for car in cars:
    print(f"{car.registration:6s}: {car.maxSpeed}, {car.odometer}")"""






