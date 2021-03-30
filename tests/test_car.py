import pytest
from Car import Car


class TestCar:

    def testCarExist(self, car):
        assert isinstance(car, Car)

    def testCarNormalWeight(self,car):
        assert car.calculateFee() == float(5.00)

    def testCarFat(self,car):
        car.weight = 1690
        assert car.calculateFee() == 5.1