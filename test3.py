from selenium import webdriver
from time import sleep
import os
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))#获取当前所在的路径
        file_path = 'file:///'+path+'/froms.html'#获取当前文件所在的路径
        # print(file_path)
        # print(path)
        self.driver.get(file_path)
    def test_login(self):
        username = self.driver.find_element_by_id('username')
        username.send_keys('langweixian')
        pwd = self.driver.find_element_by_name('pwd')
        pwd.send_keys('66666')
        print(username.get_attribute('value'))
        print(pwd.get_attribute('value'))
        self.driver.find_element_by_id('submit').click()
        self.driver.switch_to.alert.accept()#取消alert弹框
        sleep(2)
        username.clear()
        pwd.clear()

if __name__ == '__main__':
    case = TestCase()
    case.test_login()
