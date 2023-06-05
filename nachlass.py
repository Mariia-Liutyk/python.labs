class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def start_engine(self):
        print("The vehicle's engine is starting...")


class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, num_passengers):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.num_passengers = num_passengers

    def drive(self):
        print("The car is being driven...")

    def start_engine(self):
        print("The car's engine is starting...")


class Truck(Vehicle):
    def __init__(self, make, model, year, weight, cargo_capacity, towing_capacity):
        super().__init__(make, model, year, weight)
        self.cargo_capacity = cargo_capacity
        self.towing_capacity = towing_capacity

    def haul(self):
        print("The truck is hauling...")

    def start_engine(self):
        print("The truck's engine is starting...")


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, weight, num_wheels, has_sidecar):
        super().__init__(make, model, year, weight)
        self.num_wheels = num_wheels
        self.has_sidecar = has_sidecar

    def ride(self):
        print("The motorcycle is being ridden...")

    def start_engine(self):
        print("The motorcycle's engine is starting...")


car = Car("Honda", "Civic", 2022, 1200, 4, 5)
truck = Truck("Ford", "F-150", 2021, 5000, 2000, 10000)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2020, 300, 2, False)

car.start_engine()
truck.start_engine()
motorcycle.start_engine()
