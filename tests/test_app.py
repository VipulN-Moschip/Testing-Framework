import pytest
from configuration import multiply_by_two, divide_by_two, add, subtract

# Test cases mapped to TestRail Test IDs
@pytest.mark.testrail(19)
def test_multiplication(testrail_report):
    test_id = 19
    try:
        assert multiply_by_two(10) == 20
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")

@pytest.mark.testrail(20)
def test_division(testrail_report):
    test_id = 20
    try:
        assert divide_by_two(20) == 10
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")

@pytest.mark.testrail(21)
def test_addition(testrail_report):
    test_id = 21
    try:
        assert add(10, 20) == 30
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")

@pytest.mark.testrail(22)
def test_subtraction(testrail_report):
    test_id = 22
    try:
        assert subtract(6, 3) == 3
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")
