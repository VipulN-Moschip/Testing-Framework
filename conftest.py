import pytest
from configuration import TESTRAIL_URL, USERNAME, PASSWORD  # Import TestRail URL, username, and password from the config
from configuration import TEST_IDS  # Import your list of TestRail test IDs from the config
from testrail_api import TestRailAPI


# Initialize TestRail API
test_rail_api = TestRailAPI(TESTRAIL_URL, USERNAME, PASSWORD)

def update_testrail(test_id, status, comment=""):
    """
    Updates a test result in TestRail using the test ID.
    """
    try:
        response = test_rail_api.results.add_result(test_id, status_id=status, comment=comment)
        print(f"TestRail Updated: Test {test_id} -> Status {status}")
        print(f"API Response: {response}")
        return response
    except Exception as e:
        print(f"Failed to update TestRail for test {test_id}: {str(e)}")
        return None


@pytest.fixture(scope="session")
def testrail_report():
    def _report_result(test_id, status, comment=""):  # Fix: Accept 3 arguments
        update_testrail(test_id, status, comment)
    return _report_result

