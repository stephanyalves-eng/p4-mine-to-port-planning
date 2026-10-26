import pytest

from src.metrics import oee


def test_oee_multiplies_the_three_factors():
    assert oee(0.9, 0.95, 0.99) == pytest.approx(0.84645)


def test_oee_is_one_when_everything_is_perfect():
    assert oee(1, 1, 1) == 1


@pytest.mark.parametrize("factors", [(1.2, 0.9, 0.9), (0.9, -0.1, 0.9), (0.9, 0.9, 1.01)])
def test_oee_rejects_factors_outside_zero_one(factors):
    with pytest.raises(ValueError):
        oee(*factors)
