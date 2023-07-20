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


@pytest.fixture
def setup():
    print("Setup: Initializing resources")
    # Perform setup operations, e.g., setup a database connection
    # The fixture can return a value that will be available to the test functions

    yield 42  # Optional: the fixture can yield a value instead of returning it

    print("Teardown: Cleaning up resources")
    # Perform teardown operations, e.g., close the database connection

# Use the fixture in a test function


def test_example(setup):
    print("Running test_example")
    # Access the fixture value and perform the test logic
    assert setup == 42
    # ...

# Use the fixture in another test function


def test_another_example(setup):
    print("Running test_another_example")
    # Access the fixture value and perform the test logic
    assert setup == 42
    # ...
