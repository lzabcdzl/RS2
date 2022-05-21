import time
import base64


import ddddocr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://app.ringsmiley.top/")
driver.maximize_window()
driver.refresh()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "count-down").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME, "lang").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "lang-list-item").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "login-btn").click()
driver.refresh()
time.sleep(5)

#识别图形验证码
user = '100001137'
pwd = ''
expected = '请输入密码'
data = driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-image[1]/img").get_attribute('src')
data = data.replace("data:image/jpeg;base64,", "")
data = data.replace(' ', '+')
yzm = base64.b64decode(data)
ocr = ddddocr.DdddOcr()
res = ocr.classification(yzm)
print(res)

#登录
driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys(user)
time.sleep(2)
driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input").send_keys(res)
time.sleep(2)
driver.find_element(By.XPATH, '//*[@type="password"]').send_keys(pwd)
time.sleep(2)
driver.find_element(By.CLASS_NAME, "btn").click()
time.sleep(2)
WebDriverWait(driver, 5).until(EC.alert_is_present())
alert = driver.switch_to.alert
assert alert.text == expected
alert.accept()

# WebDriverWait(driver, 5).until(EC.alert_is_present())
# alert = driver.switch_to.alert
# assert alert.text == expected
# alert.accept()
time.sleep(20)

# 退出登录
driver.find_element(By.XPATH, "/html/body/uni-app/uni-tabbar/div[1]/div[5]/div/div[1]/img").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view[2]/uni-view[1]/uni-image/img").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "login-out").click()
time.sleep(5)
print("退出登录..........................")

driver.close()
driver.quit()
