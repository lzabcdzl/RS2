import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from RS2.page.login_page import LoginPage

class TestRegister(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(r"http://app.ringsmiley.top")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "count-down").click()
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "lang").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "lang-list-item").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "register-btn").click()
        self.driver.refresh()
        time.sleep(5)

    def test_register_success(self):
        try:
            youxiang = '997999@qq.com'
            yzm = '123456'
            pwd = '123456a'
            self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(youxiang)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input").send_keys(yzm)
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(pwd)
            time.sleep(2)
            self.driver.find_element(By.CLASS_NAME, "btn").click()
            time.sleep(10)
            self.driver.find_element(By.CLASS_NAME, "enter-btn").click()
            time.sleep(5)

            # 退出登录
            self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-tabbar/div[1]/div[5]/div/div[1]/img").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view[2]/uni-view[1]/uni-image/img").click()
            time.sleep(3)
            self.driver.find_element(By.CLASS_NAME, "login-out").click()
            time.sleep(5)
            print("已退出.................")
        except Exception as e:
            print(e)

    def test_register_fail(self):
        try:
            youxiang = '997998@qq.com'
            yzm = ''
            pwd = '123456a'
            expected = '请输入验证码'
            self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(youxiang)
            time.sleep(2)
            self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input").send_keys(yzm)
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(pwd)
            time.sleep(2)
            self.driver.find_element(By.CLASS_NAME, "btn").click()
            time.sleep(2)
            alert = self.driver.find_element(By.CLASS_NAME, "uni-sample-toast").text
            time.sleep(1)
            assert alert == expected
            print(True)

        except Exception as e:
            print(e)
    def tearDown(self) -> None:
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
