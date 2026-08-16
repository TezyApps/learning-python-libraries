from abc import ABC, abstractmethod

class Vehicle(ABC):

    total_vehicles: int

    def __init(self, brand):
        self.brand = brand

    def speed(self, value) -> int:
        clamped_value = max(0, min(value, 200))
        self._speed = clamped_value
        return self._speed

    def battery_level(self, value) -> int:
        if self.brand == "ElectricCar":
            self.__battery_level = value
            return self.__battery_level
        else:
            return 0

    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def fuel_type(self) -> str:
        pass

    def describe(self) -> str:
        return ", ".join([self.make_sound(), self.fuel_type()])

    def get_total_vehicles(self) -> int:
        return self.total_vehicles

class Car(Vehicle):

    def __init(self, brand, doors, speed, battery_level):
        super.__init__(brand)
        self.doors = doors
        self._speed = super().speed(speed)
        self.__battery_level = super().battery_level(battery_level)

    def make_sound(self) -> str:
        return "vroom"

    def fuel_type(self) -> str:
        return "Petrol"

class Bike(Vehicle):

    def __init(self, brand, has_carriers, speed, battery_level):
        super.__init__(brand)
        self.has_carriers = has_carriers
        self._speed = super().speed(speed)
        self.__battery_level = super().battery_level(battery_level)

    def make_sound(self) -> str:
        return "dubudubu"

    def fuel_type(self) -> str:
        return "Petrol"