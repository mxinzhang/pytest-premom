import pytest
import allure
from operation.userservice import webUserLogin
from common.logger import logger


@allure.step("步骤1 ==>> 注册用户")
def step_1(username, password, telephone, sex, address):
    logger.info("步骤1 ==>> 注册用户 ==>> {}, {}, {}, {}, {}".format(username, password, deviceID))


@allure.step("步骤2 ==>> 登录用户")
def step_2(username):
    logger.info("步骤2 ==>> 登录用户：{}".format(username))


@allure.step("步骤3 ==>> 获取某个用户信息")
def step_3(username):
    logger.info("步骤3 ==>> 获取某个用户信息：{}".format(username))


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
        username = testcase_data["email"]
        password = testcase_data["password"]
        deviceID = testcase_data["deviceID"]
        except_result = testcase_data["except_result"]
        except_code = testcase_data["except_code"]
        except_msg = testcase_data["except_msg"]
        logger.info("*************** 开始执行用例 ***************")
        result = webUserLogin(username, password, deviceID)
        step_1(username, password, deviceID)
        logger.info(result)
        assert result.success is True, result.error
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")
