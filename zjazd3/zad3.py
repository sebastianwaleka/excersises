'''
Zaimplementuj klasę ElectricCar odwzorowującą zachowanie samochodu elektrycznego.
Klasa powinna umożliwiać pokonanie zadanego dystansu, który nie może przekroczyć maksymalnego zasięgu zdefiniowanego
dla samochodu. Samochód powinien mieć także możliwość naładowania baterii.
>> car = ElectricCar(100)
>> car.drive(70)
70
>> car.drive(50)
30
>> car.drive(50)
0
>> car.charge()
>> car.drive(50)
50
'''


class ElectricCar:
    def __init__(self, energy):
        self.maxenergy = energy
        self.energy = energy

    def drive(self, distance):
        if distance < self.energy:
            self.driven = distance
        elif self.energy < 0:
            self.driven = 0
        else:
            self.driven = self.energy
        self.energy -= distance
        return self.driven

    def charge(self):
        self.energy = self.maxenergy


def test_car_drive():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0
    car.charge()
    assert car.drive(50) == 50
    car = ElectricCar(100)
    assert car.drive(200) == 100

def test_car_charge():
    car = ElectricCar(10)
    car.drive(10)
    car.charge()
    assert car.energy == 10
