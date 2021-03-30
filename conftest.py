import pytest
from Vehicle import Vehicle
from Motorbike import Motorbike
from Lorry import Lorry

@pytest.fixture
def lorry():
    return Lorry("AB1 3IE", 3000)