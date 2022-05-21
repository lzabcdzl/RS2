import logging
import unittest

from ddt import ddt, data, unpack

from RS2.base.util import Utility
from RS2.page.login_page import LoginPage


@ddt
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Utility.get_logger(level=logging.INFO,logname='RS2/report/ringsmiley.log')
        cls.page = LoginPage()
        cls.logger.info('打开浏览器')

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        cls.logger.info('关闭浏览器')

    @unpack
    @data(*Utility.get_csv_data(r'RS2/data/login_success.csv'))
    def test_login_success(self, account, password, expected):
        try:
            self.page.open('http://app.ringsmiley.top/#/pages/login/login')
            self.logger.info('打开页面')
            self.page.input_account(account)
            self.logger.info(f'输入用户名:{account}')
            self.page.input_password(password)
            self.logger.info(f'输入密码:{password}')
            self.page.click_submit()
            self.logger.info('登陆')
            self.page.wait(1)
            # assert self.page.get_realname()==expected, '断言失败'
            self.assertEqual(self.page.get_realname(), expected, '断言失败')
            self.logger.info('断言成功')
        except AssertionError as e:
            self.logger.error(f'断言失败:{self.page.get_realname()},{expected}')
            raise AssertionError(e)
        except Exception as e:
            self.logger.error('用例错误！')
            raise Exception(e)
        finally:
            self.page.click_quit()
            self.logger.info('签退')

    @unpack
    @data(*Utility.get_excel_data(r'RS2/data/login_data.xlsx', 'login_fail'))
    def test_login_fail(self, account, password, expected):
        try:
            self.page.open('http://app.ringsmiley.top/#/pages/login/login')
            if account:
                self.page.input_account(account)
            if password:
                self.page.input_password(password)
            self.page.click_submit()
            self.page.wait(1)
            self.assertEqual(self.page.get_failtip(), expected, '断言失败')
        except AssertionError as e:
            self.page.screenshot(f'test_login_fail_{account}_{password}_{expected}')
            raise AssertionError(e)
        except Exception as e:
            self.page.screenshot(f'test_login_fail_{account}_{password}_{expected}')
            raise Exception(e)
        finally:
            self.page.click_confirm()


if __name__ == '__main__':
    # for username, password in [('admin', '123456'), ('user0', '123456'), ('user1', '123456')]:
    #     LoginTest().test_login(username, password)
    unittest.main()
