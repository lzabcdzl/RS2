import logging
import unittest

from ddt import ddt, data, unpack

from RS2.base.util import Utility
from RS2.page.login_page import LoginPage


@ddt
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Utility.get_logger(level=logging.INFO, logname='E:\\ringsmiley\RS2\\report\\ringsmiley.log')
        cls.page = LoginPage()
        cls.logger.info('打开浏览器')
        cls.page.ceshi()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        cls.logger.info('关闭浏览器')

    @unpack
    @data(*Utility.get_csv_data(r'E:\ringsmiley\RS2\data\register_success.csv'))
    def test_register_success(self, user, yzm, pwd):
        try:
            self.page.click_register()
            self.page.wait(3)
            self.page.input_user(user)
            self.logger.info(f'输入用户名:{user}')
            self.page.input_yzm(yzm)
            self.logger.info(f'输入验证码:{yzm}')
            self.page.input_pwd(pwd)
            self.logger.info(f'输入密码:{pwd}')
            self.page.wait(5)
            self.page.click_login()
            self.logger.info('登陆')
            self.page.wait(3)
            self.page.click_jinru()
            self.page.wait(3)
            self.logger.info('注册成功')
            self.page.wait(1)
            self.page.click_wodeye()
            self.page.wait(1)
            self.page.click_shezhi()
            self.page.wait(1)
            self.page.click_loginout()
            self.page.wait(3)
            self.logger.info('退出登录')

        except Exception as e:
            self.logger.error('用例错误！')
            raise Exception(e)

    @unpack
    @data(*Utility.get_excel_data(r'E:\ringsmiley\RS2\data\register_data.xlsx', 'register_fail'))
    def test_register_fail(self, user, yzm, pwd, expected):
        try:
            self.page.open('http://app.ringsmiley.top')
            self.page.wait(2)
            self.page.click_tiaoguo()
            self.page.wait(3)
            self.page.click_yuyan()
            self.page.wait(2)
            self.page.click_zhongwen()
            self.page.wait(2)
            self.page.click_register()
            self.page.wait(3)
            self.page.input_user(user)
            self.page.input_yzm(yzm)
            self.page.input_pwd(pwd)
            self.page.wait(3)
            self.page.click_login()
            self.page.wait(1)
            self.assertEqual(self.page.get_assert(), expected, '断言失败')
        except AssertionError as e:
            self.page.screenshot(f'test_login_fail_{user}_{yzm}_{pwd}_{expected}')
            raise AssertionError(e)
        except Exception as e:
            raise Exception(e)


if __name__ == '__main__':
    unittest.main()
