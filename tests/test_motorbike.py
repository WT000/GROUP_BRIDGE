import pytest
from Motorbike import Motorbike


class TestMotorbikeHappy:

    def test_creation_of_motorbike_type(self, default_motorbike):
        assert default_motorbike.vehicle_type == "Motorbike"

    def test_creation_of_motorbike_reg_number(self, default_motorbike):
        assert default_motorbike.reg_num == "5050"

    def test_creation_of_motorbike_weight(self, default_motorbike):
        assert default_motorbike.weight == 150

    def test_correct_fee_return(self, default_motorbike):
        assert Motorbike.calculateFee(default_motorbike) == 3.00