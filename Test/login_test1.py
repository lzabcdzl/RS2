import base64
import time
import unittest

import ddddocr
from selenium import webdriver
from selenium.webdriver.common.by import By
from RS2.base.base_page import BasePage


class TestYongLie(unittest.TestCase):
    def setUp(self):
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
        self.driver.find_element(By.CLASS_NAME, "login-btn").click()
        self.driver.refresh()
        time.sleep(5)

    # 账号正确，验证码正确，密码正确
    def test_login_success(self):
        try:
            self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys("100001137")
            time.sleep(2)
            # #识别验证码
            data = self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-image[1]/img").get_attribute('src')
            data = data.replace("data:image/jpeg;base64,", "")
            data = data.replace(' ', '+')
            yzm = base64.b64decode(data)
            ocr = ddddocr.DdddOcr()
            res = ocr.classification(yzm)
            self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input").send_keys(res)
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("123456a")
            time.sleep(2)
            self.driver.find_element(By.CLASS_NAME, "btn").click()
            time.sleep(20)
            #退出登录
            self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-tabbar/div[1]/div[5]/div/div[1]/img").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view[2]/uni-view[1]/uni-image/img").click()
            time.sleep(3)
            self.driver.find_element(By.CLASS_NAME, "login-out").click()
            time.sleep(5)
            print("已退出.................")
        except Exception as e:
            print(e)

    #账号正确，验证码正确，密码错误
    def test_login_fail(self):
        try:
            user = '100001137'
            #识别验证码
            data = self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-image[1]/img").get_attribute('src')
            data = data.replace("data:image/jpeg;base64,", "")
            data = data.replace(' ', '+')
            res = base64.b64decode(data)
            ocr = ddddocr.DdddOcr()
            yzm = ocr.classification(res)
            pwd = '123456c'
            expected = '账号或密码错误'
            self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(user)
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

    #账号正确，验证码正确，密码格式错误
    def test_login_fail1(self):
        try:
            user = '100001137'
            # 识别验证码
            data = self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-image[1]/img").get_attribute('src')
            data = data.replace("data:image/jpeg;base64,", "")
            data = data.replace(' ', '+')
            res = base64.b64decode(data)
            ocr = ddddocr.DdddOcr()
            yzm = ocr.classification(res)
            pwd = '123456'
            expected = '密码格式错误请用字母+数字格式组成'
            self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(user)
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

    #账号正确，验证码正确，密码为空
    def test_login_fail2(self):
        try:
            user = '100001137'
            # 识别验证码
            data = self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-image[1]/img").get_attribute('src')
            data = data.replace("data:image/jpeg;base64,", "")
            data = data.replace(' ', '+')
            res = base64.b64decode(data)
            ocr = ddddocr.DdddOcr()
            yzm = ocr.classification(res)
            pwd = ''
            expected = '请输入密码'
            self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(user)
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

    # #账号错误，验证码正确，密码错误
    # def test_login_fail3(self):
    #     user = '101001137'
    #     # 识别验证码
    #     data = self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-image[1]/img").get_attribute('src')
    #     data = data.replace("data:image/jpeg;base64,", "")
    #     data = data.replace(' ', '+')
    #     res = base64.b64decode(data)
    #     ocr = ddddocr.DdddOcr()
    #     yzm = ocr.classification(res)
    #     pwd = '123456c'
    #     expected = '账号或密码错误'
    #     self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(user)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input").send_keys(yzm)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(pwd)
    #     time.sleep(2)
    #     self.driver.find_element(By.CLASS_NAME, "btn").click()
    #     time.sleep(2)
    #     alert = self.driver.find_element(By.CLASS_NAME, "uni-sample-toast").text
    #     time.sleep(1)
    #     assert alert == expected
    #     print(True)

    #账号为空，验证码正确，密码错误
    # def test_login_fail4(self):
    #     user = ''
    #     # 识别验证码
    #     data = self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-image[1]/img").get_attribute('src')
    #     data = data.replace("data:image/jpeg;base64,", "")
    #     data = data.replace(' ', '+')
    #     res = base64.b64decode(data)
    #     ocr = ddddocr.DdddOcr()
    #     yzm = ocr.classification(res)
    #     pwd = '123456c'
    #     expected = '请输入邮箱/账号'
    #     self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(user)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input").send_keys(yzm)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(pwd)
    #     time.sleep(2)
    #     self.driver.find_element(By.CLASS_NAME, "btn").click()
    #     time.sleep(2)
    #     # alert = self.driver.find_element(By.CLASS_NAME, "uni-sample-toast").text
    #     # time.sleep(1)
    #     # assert alert == expected
    #     # print(True)

    #账号为空，验证码正确，密码正确
    # def test_login_fail5(self):
    #     user = ''
    #     # 识别验证码
    #     data = self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-image[1]/img").get_attribute('src')
    #     data = data.replace("data:image/jpeg;base64,", "")
    #     data = data.replace(' ', '+')
    #     res = base64.b64decode(data)
    #     ocr = ddddocr.DdddOcr()
    #     yzm = ocr.classification(res)
    #     pwd = '123456a'
    #     expected = '请输入邮箱/账号'
    #     self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(user)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input").send_keys(yzm)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(pwd)
    #     time.sleep(2)
    #     self.driver.find_element(By.CLASS_NAME, "btn").click()
    #     time.sleep(2)
    #     # alert = self.driver.find_element(By.CLASS_NAME, "uni-sample-toast").text
    #     # time.sleep(1)
    #     # assert alert == expected
    #     # print(True)

    #账号错误，验证码正确，密码正确
    # def test_login_fail6(self):
    #     user = '101001137'
    #     # 识别验证码
    #     data = self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-image[1]/img").get_attribute('src')
    #     data = data.replace("data:image/jpeg;base64,", "")
    #     data = data.replace(' ', '+')
    #     res = base64.b64decode(data)
    #     ocr = ddddocr.DdddOcr()
    #     yzm = ocr.classification(res)
    #     pwd = '123456c'
    #     expected = '账号或密码错误'
    #     self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(user)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input").send_keys(yzm)
    #     time.sleep(2)
    #     self.driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(pwd)
    #     time.sleep(2)
    #     self.driver.find_element(By.CLASS_NAME, "btn").click()
    #     time.sleep(2)
    #     alert = self.driver.find_element(By.CLASS_NAME, "uni-sample-toast").text
    #     time.sleep(1)
    #     assert alert == expected
    #     print(True)

    #账号正确，验证码为空，密码正确
    def test_login_fail7(self):
        try:
            user = '100001137'
            yzm = ''
            pwd = '123456a'
            expected = '请输入图形验证码'
            self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(user)
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

    #账号正确，验证码错误，密码正确
    def test_login_fail8(self):
        try:
            user = '100001137'
            yzm = '1234'
            pwd = '123456a'
            expected = '图形验证码错误'
            self.driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(user)
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


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
