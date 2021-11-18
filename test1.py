from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select



class testcase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        # 获取url地址
        self.driver.get("https://www.baidu.com")
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
    def test_prop(self):
        print(self.driver.name)#获取当前使用的浏览器
        print(self.driver.current_url)#获取当前网页的url
        print(self.driver.title)#湖区当前网页的标题
        print(self.driver.window_handles)#句柄，获取当前打开的窗口，可以用于浏览器多窗口之间的切换
        print(self.driver.page_source)#获取当前页面的源码
        self.driver.quit()

    def test_method(self):
        self.driver.find_element_by_class_name("ant-btn").click()#点击申请开通
        sleep(2)
        self.driver.back()#返回上一个页面
        self.driver.refresh()#刷新页面
        self.driver.forward()#前进到返回之前的页面
        self.driver.close()#关闭当前tab
        self.driver.quit()#退出浏览器
        self.driver.switch_to.frame()#切换frame
        self.driver.switch_to.alert()#切换到alert
        self.driver.switch_to.active_element()#切换到活动元素
    #浏览器多窗口切换
    def test_windows(self):
        self.driver.find_element_by_link_text('新闻').click()
        windows = self.driver.window_handles
        while 1:
            for w in windows:
                self.driver.switch_to.window(w)
                sleep(2)




if __name__ == '__main__':
     case = testcase()
     case.test_windows()
