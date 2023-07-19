import pytest
from testcases.conftest import userservice_data


@pytest.fixture(scope="function")
def testcase_data(request):
    """
    Retrieves the testcase data for a given test case name.

    :param request: The pytest request object.
    :type request: _pytest.fixtures.SubRequest
    :return: The testcase data for the given test case name.
    :rtype: any
    """
    testcase_name = request.function.__name__
    return userservice_data.get(testcase_name)
