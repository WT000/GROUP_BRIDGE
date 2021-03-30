import pytest
from Lorry import Lorry


class TestVehicleLorryPositive:

    def test_lorry_creation(self, lorry):
        assert isinstance(lorry, Lorry)

    def test_lorry_lower_fee(self, lorry):
        assert lorry.calculateFee() == float(10.00)

    def test_lorry_higher_fee(self, lorry):
        lorry.weight = 8001
        assert lorry.calculateFee() == float(15.00)
