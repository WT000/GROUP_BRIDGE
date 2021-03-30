import pytest
from Lorry import Lorry

class TestVehicleLorryPositive:
    def test_lorry_creation(self, lorry):
        assert isinstance(lorry, Lorry)