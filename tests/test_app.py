import pytest
from configuration import multiply_by_two, divide_by_two, add, subtract

# Test cases mapped to TestRail Test IDs
@pytest.mark.testrail(19)
def test_multiplication():
    assert multiply_by_two(10) == 20

@pytest.mark.testrail(20)
def test_division():
    assert divide_by_two(20) == 10

@pytest.mark.testrail(21)
def test_addition():
    assert add(10, 20) == 30

@pytest.mark.testrail(22)
def test_subtraction():
    assert subtract(6, 3) == 3
