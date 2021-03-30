import pytest
from Motorbike import Motorbike
from Lorry import Lorry
from Bridge import Bridge


@pytest.fixture
def default_motorbike():
    yield Motorbike("Motorbike", 5050, 150)


@pytest.fixture
def lorry():
    yield Lorry("AB1 3IE", 3000)

@pytest.fixture
def bridge():
    yield Bridge()
