import pytest
from testcases.conftest import userservice_data


@pytest.fixture(scope="function")
def testcase_data(request):
    """
    This function is a fixture to retrieve testcase data.

    Args:
        request: The pytest request object. It is used to get the name of the test function.

    Returns:
        The testcase data for the requested test function. It is retrieved using the name of the test function.
    """
    return userservice_data.get(request.function.__name__)
