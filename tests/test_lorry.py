import pytest
from Lorry import Lorry

class TestVehicleLorryPositive:
    def test_lorry_creation(self):
        lorry = Lorry("AB1 3IE", 3000)
        assert isinstance(lorry, Lorry)