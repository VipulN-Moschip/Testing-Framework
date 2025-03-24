import pytest
from testrail_api import TestRailAPI
import os
import sys

os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding="utf-8")

class TestRailUtil:
    """
    A class to manage interactions with the TestRail API.
    """

    def __init__(self, test_rail_url, email, password):
        """
        Initializes the TestRailUtil class and establishes a connection to the TestRail API.
        """
        self.test_rail_api = TestRailAPI(test_rail_url, email, password)

    def add_result(self, test_id, status_id, comment=""):
        """
        Adds a test result for a specific test ID in a test run.
        """
        data = {
            "status_id": status_id,
            "comment": comment
        }
        response = self.test_rail_api.results.add_result(test_id, **data)
        return response

# TestRail Configuration
TESTRAIL_URL = "https://qa4moschip.testrail.io/"
USERNAME = "vipul.nuthalapati@moschip.com"
PASSWORD = "Moschip@123"
PROJECT_ID = 3
RUN_ID = 6
SUITE_ID = 4

# TestRail Test IDs (T11 to T18)
TEST_IDS = list(range(11, 19))

# TestRail Utility Instance
test_rail = TestRailUtil(TESTRAIL_URL, USERNAME, PASSWORD)

def update_testrail(test_id, status, comment=""):
    """
    Updates a test result in TestRail using the test ID.
    """
    try:
        response = test_rail.add_result(test_id, status, comment)
        print(f" TestRail Updated: Test {test_id} -> Status {status}")
        print(f" API Response: {response}")
        return response
    except Exception as e:
        print(f" Failed to update TestRail for test {test_id}: {str(e)}")
        return None

# Manual TestRail Connection Test
if __name__ == "__main__":
    print(" Testing TestRail connection...")
    for test_id in TEST_IDS:
        update_testrail(test_id, 1, "Test Passed Successfully")

# Pytest Fixture for TestRail Reporting
@pytest.fixture(scope="session")
def testrail_report():
    def _report_result(test_id, status, comment=""):
        update_testrail(test_id, status, comment)
    return _report_result

# Test Functions (Assertions for T11 to T18)
def test_verify_feature_one(testrail_report):
    test_id = 11
    try:
        assert 1 == 1
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")

def test_verify_feature_two(testrail_report):
    test_id = 12
    try:
        assert 2 * 2 == 4
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")

def test_verify_another_feature_one(testrail_report):
    test_id = 13
    try:
        assert 3 ** 3 == 27
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")

def test_verify_another_feature_two(testrail_report):
    test_id = 14
    try:
        assert 'hello' in 'hello world'
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")

def test_verify_subfeature_one(testrail_report):
    test_id = 15
    try:
        assert 5 + 5 == 10
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")

def test_verify_subfeature_two(testrail_report):
    test_id = 16
    try:
        assert 'sub' in 'subfolder'
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")

def test_verify_subfeature_three(testrail_report):
    test_id = 17
    try:
        assert len('list') == 4
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")

def test_verify_subfeature_four(testrail_report):
    test_id = 18
    try:
        assert 10 - 5 == 5
        testrail_report(test_id, 1, "Test passed successfully")
    except AssertionError:
        testrail_report(test_id, 5, "Test failed")
