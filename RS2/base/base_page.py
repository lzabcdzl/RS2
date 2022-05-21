import base64
import os
import time

import ddddocr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    driver = None

    def __init__(self, browser: str = 'chrome'):
        # 单例模式
        if not self.driver:
            if browser == 'chrome':
                # 成员变量
                self.driver = webdriver.Chrome()
            elif browser == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser == 'edge':
                self.driver = webdriver.Edge()
            elif browser == 'safari':
                self.driver = webdriver.Safari()
            elif browser == 'ie':
                self.driver = webdriver.Ie()

    def open(self, url, seconds=5):
        """
        打开指定的页面
        :param url: 页面地址
        :return: None
        """
        # 打开页面
        self.driver.get(url)
        # 隐式等待
        # self.driver.implicitly_wait(seconds)
        # 窗口最大化
        self.driver.maximize_window()
        #刷新页面
        self.driver.refresh()

    def converter(self, target):
        """
        将自定义元素定位方式转换为Selenium标准定位方式
        id=kw -> By.ID, "kw"
        :param target: 目标元素
        :return: 元组, (By.ID, value)
        """
        # 切分字符串
        index = target.index('=')
        # 获取定位方式和对应的值
        by, value = target[:index], target[index+1:]
        # 转换定位方式
        if by == 'id' or by == 'i':
            locator = (By.ID, value)
        elif by in ['name','n']:
            locator = (By.NAME, value)
        elif by == 'tag_name' or by == 't':
            locator = (By.TAG_NAME, value)
        elif by == 'class_name' or by == 'c':
            locator = (By.CLASS_NAME, value)
        elif by == 'link_text' or by == 'l':
            locator = (By.LINK_TEXT, value)
        elif by == 'partial_link_text' or by == 'p':
            locator = (By.PARTIAL_LINK_TEXT, value)
        elif by == 'xpath' or by == 'x':
            locator = (By.XPATH, value)
        elif by == 'css_selector' or by == 'css':
            locator = (By.CSS_SELECTOR, value)
        # 返回定位方式
        return locator

    def locate_element(self, target, timeout=5, poll_frequency=0.2):
        """
        定位单个元素
        :param target: 目标元素
        :return: WebElement
        """
        # 转换定位方式
        locator = self.converter(target)
        # 定位元素并返回
        # self.driver.find_element(locator[0],locator[1])
        # return self.driver.find_element(*locator)
        return WebDriverWait(self.driver, timeout, poll_frequency).until(expected_conditions.presence_of_element_located(locator))

    def locate_elements(self, target, timeout=5, poll_frequency=0.2):
        """
        定位多个个元素
        :param target: 目标元素
        :return: [WebElement, WebElement, ...]
        """
        # 转换定位方式
        locator = self.converter(target)
        # 定位元素并返回
        # self.driver.find_element(locator[0],locator[1])
        # return self.driver.find_element(*locator)
        return WebDriverWait(self.driver, timeout, poll_frequency)\
            .until(expected_conditions.presence_of_all_elements_located(locator))

    def type(self, target, value):
        """
        输入操作
        :param target: 目标元素
        :param value: 输入的值
        :return: None
        """
        # 定位元素
        element = self.locate_element(target)
        # 先清除文本框
        element.clear()
        # 输入内容
        element.send_keys(value)

    def click(self, target):
        """
        单击操作
        :param target: 目标元素
        :return: None
        """
        # 单击
        self.locate_element(target).click()

    def switch_to_frame(self, target):
        """
        进入iframe元素
        :param target: 目标元素
        :return: None
        """
        # 定位iframe元素
        iframe = self.locate_element(target)
        # 进入iframe元素
        self.driver.switch_to.frame(iframe)

    def select_by_index(self, target, index):
        """
        根据下标进行选择
        :param target: 目标元素
        :param index: 下标（从0开始）
        :return: None
        """
        # 定位元素
        element = self.locate_element(target)
        # 选择
        Select(element).select_by_index(index)

    def select_by_value(self, target, value):
        """
        根据value属性进行选择
        :param target: 目标元素
        :param value: value属性的值
        :return: None
        """
        # 定位元素
        element = self.locate_element(target)
        # 选择
        Select(element).select_by_value(value)

    def select_by_visible_text(self, target, visible_text):
        """
        visible_text进行选择
        :param target: 目标元素
        :param visible_text: 可见文本
        :return: None
        """
        # 定位元素
        element = self.locate_element(target)
        # 选择
        Select(element).select_by_visible_text(visible_text)

    def wait(self, seconds):
        """
        强制等待
        :param seconds: 等待的时间，单位是秒
        :return: None
        """
        time.sleep(seconds)

    def close(self):
        """
        关闭窗口
        :return: None
        """
        self.driver.close()

    def get_text(self, target):
        """
        获取指定元素的文本
        :param target: 目标元素
        :return: None
        """
        return self.locate_element(target).text

    def screenshot(self, name):
        """
        获取屏幕截图
        :param name: 截图名称
        :return: None
        """
        # 获取时间戳
        timestamp = time.strftime('%Y-%m-%d_%H-%M-%S')
        # 保存截图
        self.driver.save_screenshot(f'E:/ringsmiley/RS2/report/img/{name}_{timestamp}.png')

    def Yzm(self):
        """
        获取当前界面验证码
        :return: None
        """
        # 识别验证码
        data = self.driver.find_element(By.XPATH, "/html/body/uni-app/uni-page/uni-page-wrapper/uni-page-body/uni-view/uni-view/uni-view[2]/uni-view[3]/uni-image[1]/img").get_attribute('src')
        data = data.replace("data:image/jpeg;base64,", "")
        data = data.replace(' ', '+')
        res = base64.b64decode(data)
        ocr = ddddocr.DdddOcr()
        yzm = ocr.classification(res)
        return yzm

    def scroll(self, loc, type):
        ele = self.locator(loc)
        if type == '顶部':
            self.driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
            #滚到条到页面顶部
        elif type == '底部':
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            #滚到条到页面底部
        elif type == '窗口顶部':
            self.driver.execute_script("arguments[0].scrollIntoView();", ele)
            #滚动条到当前窗口顶部
        else:
            self.driver.execute_script("arguments[0].scrollIntoView(false);", ele)
            # 滚动条到当前窗口底部

os.system("C:\Users\lz\Documents\/22.exe")

if __name__ == '__main__':
    page = BasePage().open('http://app.ringsmiley.top')
    # page = BasePage()
    # # page.open('https://www.baidu.com')
    # r = page.locate_elements('c=mnav')
    # print(r)

