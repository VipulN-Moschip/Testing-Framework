import pytest
from configuration import TESTRAIL_URL, USERNAME, PASSWORD, TEST_IDS
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

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Pytest hook to report test results to TestRail.
    """
    outcome = yield
    report = outcome.get_result()

    # Check if the test has a TestRail marker
    testrail_marker = item.get_closest_marker("testrail")
    if testrail_marker:
        test_id = testrail_marker.args[0]  # Extract TestRail test ID
        if report.when == "call":  # Only update results after the test execution
            status = 1 if report.passed else 5  # 1 = Passed, 5 = Failed
            comment = "Test passed successfully" if report.passed else f"Test failed: {report.longrepr}"
            update_testrail(test_id, status, comment)
