class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"{self.brand} {self.model}")


class ElectricCar(Car):
    def __init__(self, brand, model, max_range, current_battery_charge):
        super().__init__(brand, model)
        self.max_range = max_range
        self.current_battery_charge = current_battery_charge

    def display_info(self):
        super().display_info()
        print(f"Max range: {self.max_range} km")
        print(f"Current battery charge is: {self.current_battery_charge}")


def get_fuel():
    if gas_car.current_fuel_level < "100%":
        print("Fueling your car to 100%...")
        gas_car.current_fuel_level = "100%"
        print("Car has a full tank")
    else:
        print("Car has a full tank already")


class GasCar(Car):
    def __init__(self, brand, model, fuel_consumption, current_fuel_level):
        super().__init__(brand, model)
        self.fuel_consumption = fuel_consumption
        self.current_fuel_level = current_fuel_level

    def display_info(self):
        super().display_info()
        print(f"Fuel consumption: {self.fuel_consumption} l/100km")
        print(f"Current fuel level is: {self.current_fuel_level}")


electric_car = ElectricCar("Tesla", "Model S", 500, "15%")
electric_car.display_info()

gas_car = GasCar("Toyota", "Camry", 8.5, "10%")
gas_car.display_info()
get_fuel()
