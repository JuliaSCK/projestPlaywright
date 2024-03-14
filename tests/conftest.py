from source.accum import Accumulator
import pytest


@pytest.fixture
def accum_global():
    return Accumulator()


@pytest.fixture(scope='function')
def accum():
    return Accumulator()
