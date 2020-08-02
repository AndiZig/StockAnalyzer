import pytest
import my_math as math


def test_add_one():
    assert math.add(2, 5) == 7


@pytest.mark.xfail
def test_add_fail():
    assert math.add(2, 3) == 4


def test_sub_one():
    assert math.sub(5, 3) == 2


@pytest.mark.xfail
def test_sub_fail():
    assert math.sub(6, 3) == 4


def test_mul_one():
    assert math.mul(5, 3) == 15


@pytest.mark.xfail
def test_mul_fail():
    assert math.mul(6, 3) == 4
