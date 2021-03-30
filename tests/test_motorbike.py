import pytest


def test_creation_of_motorbike_type(default_motorbike):
    assert default_motorbike.vehicle_type == "Motorbike"


def test_creation_of_motorbike_reg_number(default_motorbike):
    assert default_motorbike.reg_num == 5050


def test_creation_of_motorbike_weight(default_motorbike):
    assert default_motorbike.weight == 150
