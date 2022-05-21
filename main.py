"""
程序入口
"""
from RS2.runner.test_runner import TestRunner
from RS2.demo.send_email import SendEmail

class Main:
    def start(self):
        TestRunner().run()
        # SendEmail().send_email()


if __name__ == '__main__':
    Main().start()
