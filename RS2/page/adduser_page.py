from selenium.webdriver.common.by import By

from RS2.base.base_page import BasePage
import time


class AddUser(BasePage):

    def add_user(self, account, password):
        try:
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

            # # 登陆
            # self.type('id=account', 'admin')
            # self.type('id=password', '123456')
            # self.click('id=submit')
            #
            # # 添加用户
            # self.click('id=s-menu-superadmin')
            #
            # # 进入iframe
            # self.switch_to_frame('id=iframe-superadmin')
            #
            # # 点击添加成员
            # self.click('link_text=添加成员')
            # # 用户名
            # self.type('id=account', account)
            # # 真名
            # self.type('id=realname', account)
            # # 性别
            # self.click('id=genderm')
            # # 部门
            # self.select_by_index('id=dept', 2)
            # # 角色
            # self.select_by_value('id=role', 'pm')
            # # 密码
            # self.type('id=password1', password)
            # self.type('id=password2', password)
            # # 邮箱
            # self.type('id=email', "%s@163.com"%account)
            #
            # # 保存
            # self.click('id=submit')
        except Exception as e:
            print(e)
        finally:
            self.wait(2)
            self.close()


if __name__ == '__main__':
    AddUser().add_user('100000019', '123456a')
