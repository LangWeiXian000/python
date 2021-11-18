from selenium import webdriver
from time import sleep

#http://sahitest.com/demo （提供学习场景的网址）
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://sahitest.com/demo/linkTest.htm')

    def test_webelement_prop(self):
        e = self.driver.find_element_by_id('t1')
        e1 = webdriver
        print(type(e))
        print(e.id)#标识，唯一的
        print(e.tag_name)#获取标签名称
        print(e.size)#获取元素的宽高，比如search、input框等
        print(e.rect)#获取元素的宽高和坐标
        x = self.driver.find_element_by_xpath('/html/body/a[3]')
        print(x.text)#获取元素的文本内容

    def test_webelement_method(self):
        e = self.driver.find_element_by_id('t1')
        e.send_keys('hello')
        sleep(2)
        print(e.get_attribute('type'))#获取type元素里面的
        print(e.get_attribute('name'))#获取name元素里面的，如果不存在该元素，返回为空
        print(e.get_attribute('value'))#获取元素里面的value
        print(e.value_of_css_property('font'))#获取css元素里面的font字体
        print(e.value_of_css_property('color'))#获取css元素里面的颜色
        e.clear()  # 清空input框
        sleep(2)
        self.driver.quit()

    def test_method2(self):
        form_element = self.driver.find_element_by_xpath('/html/body/form[1]')#先定位到from表单
        form_element.find_element_by_id('t1').send_keys('hello world')#再定位from表单下面的id



if __name__ == '__main__':
     case = TestCase()
     case.test_method2()

