# Vehicle-management-system

class Vehicles :
    def __init__(self,vehicle_type) :
        self.vehicle_type = vehicle_type

    def vehicle_sound(self) :
        print("Vehicle makes a sound")

class Car(Vehicles) :
    def vehicle_sound(self):
        print(f"{self.vehicle_type} goes vroom vroom!")

class Bike(Vehicles) :
    def vehicle_sound(self):
        print(f"{self.vehicle_type} goes druuu druuu!")

print ("******Sounds Made by different forms of Vehicles******")
print(" ")
car = Car("Toyota")
bike = Bike("Honda-bike")
Vehicles.vehicle_sound(car)