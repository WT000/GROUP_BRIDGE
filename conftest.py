import pytest
import Motorbike


def default_motorbike():
    yield Motorbike("Motorbike", 5050, 150)