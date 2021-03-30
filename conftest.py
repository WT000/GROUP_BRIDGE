import pytest
from Vehicle import Vehicle
from Motorbike import Motorbike
from Lorry import Lorry


@pytest.fixture
def default_motorbike():
    yield Motorbike("Motorbike", 5050, 150)


@pytest.fixture
def lorry():
    yield Lorry("AB1 3IE", 3000)

