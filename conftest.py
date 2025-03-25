import pytest
import openpyxl
from datetime import datetime
from configuration import TESTRAIL_URL, USERNAME, PASSWORD, TEST_IDS, TEST_CASE_IDS
from testrail_api import TestRailAPI

# Initialize TestRail API
test_rail_api = TestRailAPI(TESTRAIL_URL, USERNAME, PASSWORD)

# ✅ List to store test results
test_results = []

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
    Pytest hook to report test results to TestRail and collect data for Excel reporting.
    """
    outcome = yield
    report = outcome.get_result()

    # Check if the test has a TestRail marker
    testrail_marker = item.get_closest_marker("testrail")
    if testrail_marker:
        test_run_id = testrail_marker.args[0]  # Extract TestRail Test Run ID
        test_case_id = TEST_CASE_IDS.get(test_run_id, test_run_id)  # Get correct Test Case ID
        
        if report.when == "call":  # Only update results after the test execution
            status = 1 if report.passed else 5  # 1 = Passed, 5 = Failed
            comment = "Test passed successfully" if report.passed else f"Test failed: {report.longrepr}"
            
            # ✅ Fetch test details using correct Test Case ID
            test_details = fetch_testrail_case(test_case_id)
            
            # ✅ Store test results for Excel
            test_results.append({
                "Test Case ID": test_case_id,
                "Test Case Name": test_details["Test Case Name"],
                "Steps": test_details["Steps"],
                "Expected Result": test_details["Expected Result"],
                "Actual Result": "Passed" if report.passed else "Failed",
                "Status": "✔" if report.passed else "❌",
                "Execution Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            # ✅ Update TestRail
            update_testrail(test_run_id, status, comment)

def fetch_testrail_case(case_id):
    """
    Fetches test case details from TestRail using the correct case ID.
    """
    try:
        response = test_rail_api.cases.get_case(case_id)
        return {
            "Test Case ID": case_id,
            "Test Case Name": response.get("title", f"Unknown (ID {case_id})"),
            "Steps": response.get("custom_steps", "No steps provided"),
            "Expected Result": response.get("custom_expected", "No expected result provided"),
        }
    except Exception as e:
        print(f"❌ Failed to fetch TestRail case {case_id}: {str(e)}")
        return {
            "Test Case ID": case_id,
            "Test Case Name": f"Unknown (ID {case_id})",
            "Steps": "Failed to fetch steps",
            "Expected Result": "Failed to fetch expected result",
        }

@pytest.fixture(scope="session", autouse=True)
def generate_excel_report():
    """
    Generates an Excel report after all tests finish.
    """
    yield  # Wait for test execution to complete

    # ✅ Create Excel workbook
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Test Results"

    # ✅ Write headers
    headers = ["Test Case ID", "Test Case Name", "Steps", "Expected Result", "Actual Result", "Status", "Execution Time"]
    sheet.append(headers)

    # ✅ Write test results to Excel
    for result in test_results:
        sheet.append(list(result.values()))

    # ✅ Save Excel report
    excel_path = "reports/test_results.xlsx"
    workbook.save(excel_path)
    print(f"📊 Excel report saved at: {excel_path}")
