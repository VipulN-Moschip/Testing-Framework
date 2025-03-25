# configuration.py

# TestRail API Configuration
TESTRAIL_URL = "https://qa4moschip.testrail.io/"
USERNAME = "vipul.nuthalapati@moschip.com"
PASSWORD = "Moschip@123"

# TestRail Test IDs (T19 to T22)
PROJECT_ID = 4         # Project ID for "Integrated Framework"
RUN_ID = 7             # Test Run ID for the test run in TestRail
SUITE_ID = 5           # Test Suite ID for the "Functional Tests"
TEST_IDS = [19, 20, 21, 22]


def multiply_by_two(a):
    return a * 2

def divide_by_two(b):
    return b / 2

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
