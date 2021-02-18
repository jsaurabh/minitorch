from minitorch import operators
from hypothesis import given
from hypothesis.strategies import lists
from .strategies import small_floats, assert_close, small_ints
import pytest


@pytest.mark.task0_1
@given(small_floats, small_floats)
def test_add_and_mul(x, y):
    assert_close(operators.mul(x, y), x * y)
    assert_close(operators.add(x, y), x + y)
    assert_close(operators.neg(x), -x)


@pytest.mark.task0_1
@given(small_floats)
def test_relu(a):
    if a > 0:
        assert operators.relu(a) == a
    else:
        assert operators.relu(a) == 0.0


## Task 0.2
## Property Testing


@pytest.mark.task0_2
@given(small_floats, small_floats)
def test_symmetric(x, y):
    assert operators.mul(x,y) == operators.mul(y, x)
    assert operators.add(x,y) == operators.add(y, x)
    assert operators.max(x,y) == operators.max(y, x)


@pytest.mark.task0_2
@given(small_ints, small_floats, small_floats)
def test_distribute(x, y, z):
    assert_close(x * (operators.relu(y) + operators.relu(z)), (x * operators.relu(y)) + (x * operators.relu(z)))
    assert_close(x * (operators.sigmoid(y) + operators.sigmoid(z)), (x * operators.sigmoid(y)) + (x * operators.sigmoid(z)))


@pytest.mark.task0_2
@given(small_floats)
def test_other(x):
    assert 0 + operators.id(x) == x
    assert x + operators.neg(x) == 0 
    assert -x + operators.neg(x) == operators.neg(operators.mul(x, 2))


# HIGHER ORDER


@pytest.mark.task0_3
@given(small_floats, small_floats, small_floats, small_floats)
def test_zip_with(a, b, c, d):
    assert_close(operators.addLists([a, b], [c, d]), [a + c, b + d])


@pytest.mark.task0_3
@given(
    lists(small_floats, min_size=5, max_size=5),
    lists(small_floats, min_size=5, max_size=5),
)
def test_property(ls1, ls2):
    assert_close(operators.add(operators.sum(ls1),\
        operators.sum(ls2)), operators.sum(ls1+ls2))


@pytest.mark.task0_3
@given(lists(small_floats))
def test_sum(ls):
    assert_close(operators.sum(ls), sum(ls))


@pytest.mark.task0_3
@given(small_floats, small_floats, small_floats)
def test_prod(x, y, z):
    assert_close(operators.prod([x, y, z]), x * y * z)
