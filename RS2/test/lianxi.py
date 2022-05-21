import logging
import os
import unittest

from ddt import ddt, data, unpack

from RS2.base.util import Utility
from RS2.page.login_page import LoginPage


@ddt
class XiaoxiTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.logger = Utility.get_logger(level=logging.INFO, logname='E:\\ringsmiley\RS2\\report\\lianxi.log')
        cls.page = LoginPage()
        cls.logger.info('打开浏览器')
        cls.page.open('http://app.ringsmiley.top')
        cls.logger.info('打开页面')
        cls.page.wait(2)
        cls.page.click_tiaoguo()
        cls.page.wait(3)
        cls.page.click_yuyan()
        cls.page.wait(2)
        cls.page.click_zhongwen()
        cls.page.wait(2)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.page.close()
        cls.logger.info('关闭浏览器')

    @unpack
    @data(*Utility.get_csv_data(r'E:\ringsmiley\RS2\data\xiaoxi.csv'))
    def test_Fafddd(self, user, pwd):
        try:
            self.page.click_loginin()
            self.page.wait(3)
            self.page.input_user(user)
            self.logger.info(f'输入用户名:{user}')
            yzm = self.page.Yzm()
            self.page.input_yzm(yzm)
            self.logger.info(f'输入验证码:{yzm}')
            self.page.input_pwd(pwd)
            self.logger.info(f'输入密码:{pwd}')
            self.page.wait(3)
            self.page.click_login()
            self.logger.info('登陆')
            self.page.wait(5)
            try:
                self.page.click_shouye()
            except:
                self.page.input_yzm(yzm)
                self.logger.info(f'重新输入验证码:{yzm}')
                self.page.wait(2)
                self.page.click_login()
                self.logger.info(f'重新登录')
                self.page.wait(5)
            self.page.click_shouye()
            self.page.wait(2)
            self.logger.info('登录成功')
            self.page.click_xiaoxi()
            self.page.wait(5)
            self.page.click_xxshijain()
            self.page.wait(5)
            self.page.click_faxiaoxi()
            self.page.wait(2)
            self.page.click_xiangce()
            self.page.wait(2)
            self.page.click_fufeifa()
            self.page.wait(3)
            os.system("C:\Users\lz\Documents\/22.exe")
            self.page.wait(5)
            self.page.click_fanhui()
            self.page.wait(3)
            # 退出登录
            self.page.click_wodeye()
            self.page.wait(1)
            self.page.click_shezhi()
            self.page.wait(1)
            self.page.click_loginout()
            self.page.wait(5)
            self.logger.info('退出登录')

        except Exception as e:
            self.logger.error(f'用例错误！{e}')
            raise Exception(e)


if __name__ == '__main__':
    XiaoxiTest().test_Fafddd()
