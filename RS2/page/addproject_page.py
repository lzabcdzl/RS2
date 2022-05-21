import base64
import random

import ddddocr
from selenium import webdriver
from time import sleep, time

from selenium.webdriver.common.by import By

from RS2.base.base_page import BasePage


class AddProject(BasePage):

    def add_project(self):
        # # 点击项目
        # self.click('id=s-menu-3')
        # # 进入iframe
        # self.switch_to_frame('id=iframe-3')
        # # 点击添加区块
        # self.click('p=添加区块')
        # # 区块
        # self.select_by_value('id=blocks', 'task')
        # # 区块名称
        # heading = 'block7'
        # self.type('id=title', heading)
        # # 宽度
        # self.select_by_index('id=grid', random.randint(0, 5))
        # # 颜色
        # self.click('xpath=//*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/button')
        # self.click('xpath=//*[@id="ajaxForm"]/table/tbody/tr[2]/td/div/div/div/div/li[%d]/button'%random.randint(1, 6))
        # # 状态
        # self.click('id=paramsstatus_chosen')
        # self.click('xpath=//*[@id="paramsstatus_chosen"]/div/ul/li[%d]'%random.randint(1, 4))
        # # 数量
        # self.type('id=params[num]', 20)
        # # 排序
        # self.click('id=paramsorderBy_chosen')
        # self.click('xpath=//*[@id="paramsorderBy_chosen"]/div/ul/li[%d]'%random.randint(1, 6))
        # # 保存
        # self.click('id=submit')
        # sleep(2)
        # # 断言
        # elements = self.locate_elements('c=panel-heading')
        # headings = [e.text for e in elements]
        # print(headings)
        # assert '更多\n'+heading in headings, '添加失败'

        # 关闭当前窗口
        self.close()


if __name__ == '__main__':
    AddProject().add_project()
