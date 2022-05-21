import time
import unittest

from RS2.base.HTMLTestRunner import HTMLTestRunner


class TestRunner:

    def run(self):
        """
        用例运行器
        :return:
        """
        # 创建测试套件对象
        suite = unittest.TestSuite()
        # 添加用例
        suite.addTests(unittest.TestLoader().discover(r'E:\ringsmiley\RS2\test', pattern='xiaoxi_test.py'))
        # 创建报告
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        report = open(r'RS2/report/report_%s.html' % timestamp, 'wb')
        # 创建用例运行器
        runner = HTMLTestRunner(stream=report, title='RS2自动化测试报告', description='报告的详细描述....')
        # 运行用例，生成报告
        runner.run(suite)
        # 发送报告


if __name__ == '__main__':
    TestRunner().run()
