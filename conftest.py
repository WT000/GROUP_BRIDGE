import pytest
from Motorbike import Motorbike
from Lorry import Lorry
from Car import Car
from Bridge import Bridge



@pytest.fixture
def default_motorbike():
    yield Motorbike("Motorbike", 5050, 150)


@pytest.fixture
def lorry():
    yield Lorry("AB1 3IE", 3000)

@pytest.fixture
def car():
    yield Car("A6423KM", 1234, "Car")

@pytest.fixture
def bridge():
    yield Bridge()

