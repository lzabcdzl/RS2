import time
import re

# import np as np
from PIL import Image
import pytesseract
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://app.ringsmiley.top")
driver.maximize_window()
driver.refresh()
time.sleep(2)
# driver.refresh()
# time.sleep(6)
# #对页面截图
# driver.save_screenshot('login.png')
# #选择验证码图片的元素
# yzm = driver.find_element(By.CLASS_NAME, "code-image")
# #获取图片元素的位置
# loc = yzm.location
# #获取图片的宽高
# size = yzm.size
# #获取验证码上下左右的位置
# left = loc['x']
# top = loc['y']
# right = (loc['x'] + size['width'])
# botom = (loc['y'] + size['height'])
# val = (left, top, right, botom)
# #打开网页截图
# login_pic = Image.open('login.png')
# #截取验证码
# yzm = login_pic.crop(val)
# #保存验证码
# img = yzm.convert("L")  # 转灰度
# # array = np.array(img)
# # img1 = Image.fromarray(array.astype('uint8'))
# # img1 = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", img)     #去除识别出来的特殊字符
# # img = result[0:4]  # 只获取前四个字符
# # pixdata = img.load()
# # w, h = img.size
# # threshold = 160
# # # 遍历所有像素，大于。。值的为黑色
# # for y in range(h):
# #     for x in range(w):
# #         if pixdata[x, y] < threshold:
# #             pixdata[x, y] = 0
# #         else:
# #             pixdata[x, y] = 255
# img.save('yzm.png')
# #识别验证码
# pytesseract.pytesseract.tesseract_cmd = r"D:\Tesseract-OCR\tesseract.exe"
# yzm1 = Image.open('yzm.png')
# # yzm1.show()
# # pixdata = yzm1.load()
# # for y in range(yzm1.size[1]):
# #     for x in range(yzm1.size[0]):
# #         if pixdata[x, y]>30 or pixdata[x, y][1] >30 or pixdata[x, y][2]>30 or pixdata[x, y][3] == 0:
# #             pixdata[x, y] = (255, 255, 255, 255)
# # yzm1.show()
# result = pytesseract.image_to_string(yzm1, lang='chi_sim')
# res = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", " ", result)
# print(res)
#
# #登录
# driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys("100000019")
# time.sleep(2)
# driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input").send_keys(res)
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("123456a")
# time.sleep(2)
# driver.find_element(By.CLASS_NAME, "btn").click()
# time.sleep(10)
# # 退出登录
# driver.find_element(By.XPATH, "/html/body/uni-app/uni-tabbar/div[1]/div[5]/div/div[1]/img").click()
# time.sleep(3)
# driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view[2]/uni-view[1]/uni-image/img").click()
# time.sleep(3)
# driver.find_element(By.CLASS_NAME, "login-out").click()
# time.sleep(5)
# print("退出登录..........................")

driver.close()
driver.quit()

