import pytest
from Car import Car


class TestCar:

    def testCarExist(self, car):
        assert isinstance(car, Car)

    def testCarNormalWeight(self, car):
        assert car.calculateFee() == float(5.00)

    def testCarExactOverweight(self, car):
        car.weight = 1690
        assert car.calculateFee() == 5.1
        
    def testCarBeforeOverweight(self, car):
        car.weight = 1689
        assert car.calculateFee() == 5.0
        
    def testCarAfterOverweight(self, car):
        car.weight = 1691
        assert car.calculateFee() == 5.1
        
    def testCarSecondOverweight(self, car):
        car.weight = 1790
        assert car.calculateFee() == 5.2
