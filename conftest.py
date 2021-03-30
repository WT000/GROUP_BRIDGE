import pytest
from Motorbike import Motorbike
from Vehicle import Vehicle


@pytest.fixture
def default_motorbike():
    yield Motorbike("Motorbike", 5050, 150)
