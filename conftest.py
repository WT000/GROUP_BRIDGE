import pytest
from Motorbike import Motorbike
from Lorry import Lorry
<<<<<<< HEAD
from Car import Car
=======
from Bridge import Bridge
>>>>>>> 17fd87328541c394427f298aba725b1a00341d0c


@pytest.fixture
def default_motorbike():
    yield Motorbike("Motorbike", 5050, 150)


@pytest.fixture
def lorry():
    yield Lorry("AB1 3IE", 3000)

@pytest.fixture
<<<<<<< HEAD
def car():
    yield Car("A6423KM", 1234, "Car")
=======
def bridge():
    yield Bridge()
>>>>>>> 17fd87328541c394427f298aba725b1a00341d0c
