from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select



class testcase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # 获取url地址
        self.driver.get("https://wecard.qq.com/pc/login")
        self.driver.maximize_window()
        sleep(3)

    def test_NoserviceApply(self):
        self.driver.find_element_by_class_name("ant-btn").click()
        sleep(1)
        self.driver.find_element_by_class_name("_23UJSqRgE__T3-G04vGRV_").click()
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="industry-container"]/div[1]/div/span[2]').click()#点击行业类型父下拉框
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="industry-container"]/div[3]/div/div/div/div[2]/div[1]/div/div/div[1]').click()#点击下拉框选项
        self.driver.find_element_by_xpath('//*[@id="industry-container"]/div[2]/div/span[2]').click()#点击行业类型子下拉框
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="industry-container"]/div[4]/div/div/div/div[2]/div[1]/div/div/div[2]/div').click()#点击下拉框选项
        sleep(1)
        self.driver.find_element_by_id("school_name").send_keys("无服务号测试000001")
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="registContainer"]/form/div[1]/div[1]/div[3]/div[2]/div/span/div/div/span[2]').click()#点击人员规模下拉框
        self.driver.find_element_by_xpath('//*[@id="registContainer"]/div/div/div/div/div[2]/div[1]/div/div/div[3]').click()#点击选择人员规模下拉框人数100-200人
        self.driver.find_element_by_id('name').send_keys('test')





if __name__ == '__main__':
     case = testcase()
     case.test_NoserviceApply()
