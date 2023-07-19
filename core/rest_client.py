import requests
import json as complexjson
from common.logger import logger

# Define a RestClient class


class RestClient():
    session = requests.session()
    request_methods = {
        "GET": session.get,
        "POST": session.post,
        "PUT": session.put,
        "DELETE": session.delete,
        "PATCH": session.patch
    }

    def __init__(self, api_root_url):
        self.api_root_url = api_root_url

    def request(self, url, method, data=None, json=None, **kwargs):
        """
        Sends a request to the specified URL using the specified method.

        :param url: The URL to send the request to.
        :type url: str
        :param method: The HTTP method to use for the request.
        :type method: str
        :param data: The data to include in the request body.
        :type data: dict, optional
        :param json: The JSON data to include in the request body.
        :type json: dict, optional
        :param kwargs: Additional keyword arguments to pass to the request method.

        :return: The response from the server.
        :rtype: requests.Response

        :raises ValueError: If an invalid request method is specified.
        """
        url = self.api_root_url + url
        headers = kwargs.get("headers")
        params = kwargs.get("params")
        files = kwargs.get("files")
        cookies = kwargs.get("cookies")
        self.request_log(url, method, data, json, params, headers, files, cookies)

        request_func = self.request_methods.get(method)
        if request_func:
            return request_func(url, data=data, json=json, **kwargs)
        else:
            raise ValueError(f"Invalid request method: {method}")

    @classmethod
    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        """
            Log the request details.

            Args:
                url (str): The URL for the request.
                method (str): The HTTP method for the request.
                data (dict): The data to send in the request body.
                json (dict): The JSON data to send in the request body.
                params (dict): The query parameters for the request.
                headers (dict): The headers for the request.
                files (dict): The files to send in the request.
                cookies (dict): The cookies to send with the request.
        """
        # Log the URL of the API request
        logger.info("API request URL ==>> {}".format(url))
        # Log the HTTP method of the API request
        logger.info("API request method ==>> {}".format(method))
        # Log the headers of the API request as JSON string
        logger.info("API request headers ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        # Log the params of the API request as JSON string
        logger.info("API request params ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        # Log the data parameter of the API request as JSON string
        logger.info("API request data parameter ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        # Log the json parameter of the API request as JSON string
        logger.info("API request json parameter ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        # Log the files parameter of the API request
        logger.info("API request files parameter ==>> {}".format(files))
        # Log the cookies parameter of the API request as JSON string
        logger.info("API request cookies parameter ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))
        # TODO: Log the kwargs of the API request as JSON string
        logger.info("API request kwargs ==>> {}".format(complexjson.dumps(kwargs, indent=4, ensure_ascii=False)))
