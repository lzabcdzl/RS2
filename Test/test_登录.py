import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(r"http://app.ringsmiley.top")
        time.sleep(2)
    # 账号正确，密码正确
    def test_login_success(self):
        self.driver.find_element(By.CLASS_NAME, "count-down").click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "lang").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "lang-list-item").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "login_account").click()
        time.sleep(2)

        # 账号登录
        self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys("100000019")
        time.sleep(10)
        # driver.find_element(By.CLASS_NAME, "verification").send_keys("")
        # time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("123456a")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        time.sleep(5)
        print("恭喜您登录成功，请开始操作.....................")
        print("---------------------------------------------------------------------------")
        # 退出登录
        self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-tabbar/div[1]/div[5]/div/div[1]/img").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view[2]/uni-view[1]/uni-image/img").click()
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, "login-out").click()
        time.sleep(5)
        print("您已退出登录")
        print("---------------------------------------------------------------------------")
        pass

    #账号正确，密码错误
    def test_login_fail1(self):
        self.driver.find_element(By.CLASS_NAME, "count-down").click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "lang").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "lang-list-item").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "login_account").click()
        time.sleep(2)
        # 账号登录
        self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys("100000019")
        time.sleep(10)
        # driver.find_element(By.CLASS_NAME, "verification").send_keys("")
        # time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("123456b")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        time.sleep(5)
        print("账号或密码错误.....................")
        print("---------------------------------------------------------------------------")
        pass

    #账号正确，密码格式错误
    def test_login_fai2(self):
        self.driver.find_element(By.CLASS_NAME, "count-down").click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "lang").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "lang-list-item").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "login_account").click()
        time.sleep(2)
        # 账号登录
        self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys("100000019")
        time.sleep(10)
        # driver.find_element(By.CLASS_NAME, "verification").send_keys("")
        # time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("123456b")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        time.sleep(5)
        print("密码格式错误请用字母+数字组成.....................")
        print("---------------------------------------------------------------------------")
        pass

    #账号错误，密码正确
    def test_login_fail3(self):
        self.driver.find_element(By.CLASS_NAME, "count-down").click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "lang").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "lang-list-item").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "login_account").click()
        time.sleep(2)
        # 账号登录
        self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys("200000019")
        time.sleep(10)
        # driver.find_element(By.CLASS_NAME, "verification").send_keys("")
        # time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("123456a")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        time.sleep(5)
        print("账号或密码错误.....................")
        print("---------------------------------------------------------------------------")
        pass

    #账号为空，密码为空
    def test_login_fail4(self):
        self.driver.find_element(By.CLASS_NAME, "count-down").click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "lang").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "lang-list-item").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "login_account").click()
        time.sleep(2)
        # 账号登录
        self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys("")
        time.sleep(10)
        # driver.find_element(By.CLASS_NAME, "verification").send_keys("")
        # time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        time.sleep(5)
        print("请输入您的账号.....................")
        print("---------------------------------------------------------------------------")
        pass

    #账号正确，密码为空
    def test_login_fail5(self):
        self.driver.find_element(By.CLASS_NAME, "count-down").click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "lang").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "lang-list-item").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "login_account").click()
        time.sleep(2)
        # 账号登录
        self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys("100000019")
        time.sleep(10)
        # driver.find_element(By.CLASS_NAME, "verification").send_keys("")
        # time.sleep(2)
        self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "btn").click()
        time.sleep(5)
        print("请输入您的密码.....................")
        print("---------------------------------------------------------------------------")
        pass

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
