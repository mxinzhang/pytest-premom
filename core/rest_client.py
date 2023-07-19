import requests
import json as complexjson
from common.logger import logger


class RestClient():
    """_summary_
      api_root_url : str = setting.ini["host"]["api_root_url"]
      session : requests.Session = requests.Session()
    """
    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def get(self, url, **kwargs):
        """
        Sends a GET request to the specified URL.

        Parameters:
            url (str): The URL to send the GET request to.
            **kwargs: Additional keyword arguments to be passed to the request method.

        Returns:
            The response from the GET request.
        """
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        """
        Sends a POST request to the specified URL.

        Args:
            url (str): The URL to send the request to.
            data (dict, optional): The data to send in the request body. Defaults to None.
            json (dict, optional): The JSON data to send in the request body. Defaults to None.
            **kwargs: Additional keyword arguments to be passed to the request method.

        Returns:
            The response from the request.

        Raises:
            Any exceptions raised by the underlying request method.
        """
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        """
        Sends a PUT request to the specified URL.

        Parameters:
            url (str): The URL to send the request to.
            data (dict, optional): The data to send with the request. Defaults to None.
            **kwargs: Additional keyword arguments to be passed to the request method.

        Returns:
            The response from the request.
        """
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        """
        Deletes a resource at the specified URL using an HTTP DELETE request.

        Args:
            url (str): The URL of the resource to be deleted.
            **kwargs: Additional keyword arguments to be passed to the `request` method.

        Returns:
            The response from the `request` method.

        Raises:
            Any exceptions raised by the `request` method.
        """
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        """
        Send a PATCH request to the specified URL.

        :param url: The URL to send the PATCH request to.
        :type url: str
        :param data: The data to be included in the request body (optional).
        :type data: dict or str or bytes
        :param kwargs: Additional keyword arguments to be passed to the request method.
        :type kwargs: any
        :return: The response of the PATCH request.
        :rtype: Response
        """
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        """
        Sends an HTTP request to the specified URL using the specified method.

        Args:
            url (str): The URL to send the request to.
            method (str): The HTTP method to use for the request.
            data (str, optional): The data to send in the request body. Defaults to None.
            json (dict, optional): A JSON object to send in the request body. Defaults to None.
            **kwargs: Additional keyword arguments to pass to the underlying HTTP library.

        Returns:
            requests.Response: The response object containing the server's response to the request.

        Raises:
            None.
        """
        # Special case for allmethod requests
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return requests.post(url, data, json, **kwargs)
        if method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        """
        Logs the details of an API request.

        Args:
            url (str): The URL of the API request.
            method (str): The HTTP method used for the request.
            data (dict, optional): The data payload for the request. Defaults to None.
            json (dict, optional): The JSON payload for the request. Defaults to None.
            params (dict, optional): The query parameters for the request. Defaults to None.
            headers (dict, optional): The headers for the request. Defaults to None.
            files (dict, optional): The files to be uploaded with the request. Defaults to None.
            cookies (dict, optional): The cookies for the request. Defaults to None.
            **kwargs: Additional keyword arguments.

        Returns:
            None
        """
        logger.info("api request address ==>> {}".format(url))
        logger.info("api request method ==>> {}".format(method))
        logger.info("api request headers ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("api request params ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("api request body data param ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("api request body json param ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        logger.info("api upload files param ==>> {}".format(files))
        logger.info("api cookies param ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))
