from abc import ABC, abstractmethod

def __clamped(value: int, min_value: int = 0, max_value: int = 200) -> int:
    return max(min_value, min(value, max_value))

class Vehicle(ABC):

    total_vehicles: int

    def __init(self, brand):
        self.brand = brand
        self._speed = 0
        self.__battery_level = 0
        Vehicle.total_vehicles += 1

    #region - Properties:

    @property 
    def speed(self) -> int:
        return self._speed

    @speed.setter
    def speed(self, value: int) -> int:
        self._speed = __clamped(value)
        return self._speed

    @property 
    def battery_level(self) -> int:
        return self.__battery_level

    @battery_level.setter
    def battery_level(self, value: int) -> int:
        self.__battery_level = __clamped(value)
        return self.__battery_level

    #endregion

    #region - Abstract Methods

    @abstractmethod
    def make_sound(self) -> str:
        pass

    @abstractmethod
    def fuel_type(self) -> str:
        pass

    #endregion

    #region - Concrete Methods

    def describe(self) -> str:
        return ", ".join([self.make_sound(), self.fuel_type()])

    #endregion

    #region - Class Methods

    @classmethod
    def get_total_vehicles(cls) -> int:
        return cls.total_vehicles

    #endregion

class Car(Vehicle):

    def __init(self, brand, doors, speed, battery_level):
        super.__init__(brand)
        self.doors = doors

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