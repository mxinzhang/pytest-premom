import os
from core.rest_client import RestClient
from common.read_data import data

# Get the base path of the project
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Construct the path to the data file
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")

# Load the API root URL from the data file
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class UserService(RestClient):
    """Class representing the user service API"""

    def __init__(self, api_root_url, **kwargs):
        """
        Initialize the UserService.

        Args:
            api_root_url (str): The root URL of the API.
            **kwargs: Additional keyword arguments.
        """
        super(UserService, self).__init__(api_root_url, **kwargs)

    def webUserLogin(self, **kwargs):
        """
        Make a POST request to the "/user/web/sign/in" endpoint.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            The response from the API.
        """
        return self.post("/user/web/sign/in", **kwargs)

    def thirdUserLogin(self, **kwargs):
        """
        Make a POST request to the "/user/web/sign/in/third" endpoint.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            The response from the API.
        """
        return self.post("/user/web/sign/in/third", **kwargs)

    def webRegister(self, **kwargs):
        """
        Make a POST request to the "/user/web/sign/up" endpoint.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            The response from the API.
        """
        return self.post("/user/web/sign/up", **kwargs)


# Create an instance of the UserService
userservice = UserService(api_root_url)
