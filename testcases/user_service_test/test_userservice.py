import pytest
import allure
from operation.userservice import webUserLogin
from common.logger import logger


@allure.severity(allure.severity_level.CRITICAL)
@allure.epic("针对业务场景的测试")
@allure.feature("场景：用户注册-用户登录-查看用户")
class TestRegLogList():
    @allure.story("用例--注册/登录/查看--预期成功")
    @allure.description("该用例是针对 注册-登录-查看 场景的测试")
    @allure.issue("", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("", name="点击，跳转到对应用例的链接地址")
    @allure.title("用户注册登录查看-预期成功")
    @pytest.mark.multiple
    def test_userservice_login(self, testcase_data):
        """
        Test the user service login functionality with expected success.

        :param testcase_data: The data for the test case.
        :type testcase_data: dict

        This function performs a test on the user service login functionality. It takes in the `testcase_data` parameter, which is a dictionary containing the necessary data for the test case. The `testcase_data` dictionary should have the following keys:

        - `email`: The email of the user.
        - `password`: The password of the user.
        - `deviceID`: The device ID of the user.
        - `except_result`: The expected result of the test case.
        - `except_code`: The expected code of the test case.
        - `except_msg`: The expected message of the test case.

        The function starts by logging the beginning of the test case execution. It then calls the `webUserLogin` function with the provided `username`, `password`, and `deviceID`. The result of the function call is stored in the `result` variable.

        The function asserts that the `result.success` attribute is `True` and raises an error if it is not. It also asserts that the `result.success` attribute is equal to the `except_result` value and raises an error if it is not.

        The function logs the expected code and compares it with the actual code from the response. If they are not equal, an assertion error is raised. The function also asserts that the `except_msg` is present in the result message.

        Finally, the function logs the end of the test case execution.

        """
        username = testcase_data["email"]
        password = testcase_data["password"]
        deviceID = testcase_data["deviceID"]
        except_result = testcase_data["except_result"]
        except_code = testcase_data["except_code"]
        except_msg = testcase_data["except_msg"]
        logger.info("*************** 开始执行用例 ***************")
        result = webUserLogin(username, password, deviceID)
        assert result.success is True, result.error
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")
