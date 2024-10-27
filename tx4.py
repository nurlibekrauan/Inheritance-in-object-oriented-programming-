class Vehicle:
    def __init__(self, speed, mileage):
        self.speed = speed
        self.mileage = mileage

    def move(self):
        raise NotImplementedError("Этот метод должен быть переопределён в подклассах")


class Car(Vehicle):
    def __init__(self, speed, mileage, fuel):
        super().__init__(speed, mileage)
        self.fuel = fuel

    def move(self):
        # Примерная логика расчета расхода топлива
        fuel_cons = self.mileage / self.fuel
        return f'Car is moving with fuel consumption of {fuel_cons:.2f} miles per gallon'


class Bicycle(Vehicle):
    def __init__(self, speed, mileage, gear):
        super().__init__(speed, mileage)
        self.gear = gear

    def move(self):
        # Влияние передач на движение велосипеда
        efficiency = self.gear * 0.1  # Пример влияния передачи на эффективность
        distance_per_pedal = self.speed * efficiency
        return f'Bicycle is moving at {distance_per_pedal:.2f} miles per pedal with gear {self.gear}'


car = Car(speed=100, mileage=20000, fuel=50)
bicycle = Bicycle(speed=20, mileage=500, gear=3)

print(car.move())  # Учитывая расход топлива
print(bicycle.move())  # Учитывая передачу
