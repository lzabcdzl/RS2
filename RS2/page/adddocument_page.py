import base64

import ddddocr
from selenium import webdriver
from time import sleep, time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

try:
    driver = webdriver.Chrome()
    driver.get('http://app.ringsmiley.top')
    driver.maximize_window()
    driver.implicitly_wait(5)
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
    #登录
    driver.find_element(By.CLASS_NAME, "uni-input-input").send_keys("100001137")
    time.sleep(2)
    # 识别验证码
    data = driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-image[1]/img").get_attribute('src')
    data = data.replace("data:image/jpeg;base64,", "")
    data = data.replace(' ', '+')
    yzm = base64.b64decode(data)
    ocr = ddddocr.DdddOcr()
    res = ocr.classification(yzm)
    driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-input/div/input").send_keys(res)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@type="password"]').send_keys("123456a")
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "btn").click()
    time.sleep(20)
    # 退出登录
    driver.find_element(By.XPATH, "/html/body/uni-app/uni-tabbar/div[1]/div[5]/div/div[1]/img").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view[1]/uni-view/uni-view[2]/uni-view[1]/uni-image/img").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME, "login-out").click()
    time.sleep(5)
    print("已退出.................")

    # # 登陆
    # driver.find_element(By.ID, 'account').send_keys('admin')
    # driver.find_element(By.ID, 'password').send_keys('123456')
    # driver.find_element(By.ID, 'submit').click()
    #
    # # 点击 添加文档
    # driver.find_element(By.ID, 's-menu-4').click()
    #
    # # 进入iframe
    # iframe = driver.find_element(By.ID, 'iframe-4')
    # driver.switch_to.frame(iframe)
    #
    # # 点击 创建文档库
    # driver.find_element(By.PARTIAL_LINK_TEXT, '创建文档库').click()
    #
    # # 选择文档库类型
    # Select(driver.find_element(By.ID, 'libType')).select_by_value('custom')
    #
    # # 文档库名称
    # name = 'Python基础'
    # driver.find_element(By.ID, 'name').send_keys(name)
    #
    # # 授权用户
    # driver.find_element(By.XPATH, '//*[@id="users_chosen"]/ul').click()
    # driver.find_element(By.XPATH, '//*[@id="users_chosen"]/div/ul/li[3]').click()
    #
    # # 授权分组
    # driver.find_element(By.ID, 'groups1').click()
    # driver.find_element(By.ID, 'groups3').click()
    # driver.find_element(By.ID, 'groups5').click()
    #
    # # 保存
    # driver.find_element(By.ID, 'submit').click()
    #
    # # 维护分类
    # driver.find_element(By.LINK_TEXT, '维护分类').click()
    # driver.find_element(By.NAME, 'children[1]').send_keys('Python基础')
    # driver.find_element(By.NAME, 'children[2]').send_keys('Python爬虫')
    # driver.find_element(By.NAME, 'children[3]').send_keys('Python运维')
    # driver.find_element(By.NAME, 'children[4]').send_keys('Python自动化')
    # # 保存分类
    # driver.find_element(By.ID, 'submit').click()
    #
    # driver.find_element(By.LINK_TEXT, name).click()
    #
    # # 创建文档
    # driver.find_element(By.PARTIAL_LINK_TEXT, '创建文档').click()
    #
    # # 所属分类
    # Select(driver.find_element(By.ID, 'module')).select_by_index(1)
    #
    # # 授权用户
    # driver.find_element(By.XPATH, '//*[@id="users_chosen"]/ul').click()
    # sleep(1)
    # driver.find_element(By.XPATH, '//li[contains(text(), "user1")]').click()
    # # driver.find_element(By.XPATH, '//*[@id="users_chosen"]/div/ul/li[3]').click()
    #
    # # 授权分组
    # driver.find_element(By.ID, 'groups1').click()
    # driver.find_element(By.ID, 'groups3').click()
    # driver.find_element(By.ID, 'groups5').click()
    #
    # # 文档类型
    # driver.find_element(By.ID, 'typetext').click()
    # # 文档标题
    # driver.find_element(By.ID, 'title').send_keys('高阶函数')
    # # 文档正文
    # driver.switch_to.frame(driver.find_element(By.ID, 'ueditor_0'))
    # driver.find_element(By.XPATH, '/html/body/p').send_keys('Python高级函数可以接收....')
    # driver.switch_to.parent_frame()
    #
    # # 关键字
    # driver.find_element(By.ID, 'keywords').send_keys('函数')
    #
    # # 摘要
    # driver.find_element(By.ID, 'digest').send_keys('函数可以作为参数，也可以作为返回值')
    #
    # driver.find_element(By.XPATH, '//*[@id="fileBox1"]/tbody/tr/td[1]/div/input').send_keys(r'D:\岳飞.jpg')
    # driver.find_element(By.XPATH, '//*[@id="fileBox2"]/tbody/tr/td[1]/div/input').send_keys(r'D:\岳飞.jpg')
    #
    # # 保存
    # driver.find_element(By.ID, 'submit').click()

except Exception as e:
    print(e)
finally:
    sleep(2)
    driver.close()
