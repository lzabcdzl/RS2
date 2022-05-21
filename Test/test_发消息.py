import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://app.ringsmiley.top")
time.sleep(3)
driver.find_element(By.CLASS_NAME, "count-down").click()
time.sleep(6)
driver.find_element(By.CLASS_NAME, "lang").click()
time.sleep(1)
driver.find_element(By.CLASS_NAME, "lang-list-item").click()
time.sleep(2)
driver.find_element(By.CLASS_NAME, "login_account").click()
time.sleep(2)

#账号登录
driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys("100000019")
time.sleep(10)
driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("123456a")
time.sleep(2)
driver.find_element(By.CLASS_NAME, "btn").click()
time.sleep(5)
print("登录成功....................")
#点击消息列表
driver.find_element(By.XPATH, "/html/body/uni-app/uni-tabbar/div[1]/div[3]/div/div[1]/img").click()

#页面滚动
js = "window.scrollTo(0,1000)"
driver.execute_script(js)
time.sleep(2)
#持续滚动条下拉操作
for i in range(20):
    js_1 = "window.scrollTo(0,%s)" % (i * 100)
    driver.execute_script(js_1)
    time.sleep(2)

# #持续往回滚动（上拉）
# for i in range(20):
#     js_2 = "var q = document.documentElement.scrollTop = %s" % (2000 - i * 100)
#     driver.execute_script(js_2)
#     time.sleep(2)

#退出登录
driver.find_element(By.XPATH, "/html/body/uni-app/uni-tabbar/div[1]/div[5]/div/div[1]/img").click()
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view[2]/uni-view[1]/uni-image/img").click()
time.sleep(3)
driver.find_element(By.CLASS_NAME, "login-out").click()
time.sleep(5)
print("退出登录..........................")


driver.quit()
