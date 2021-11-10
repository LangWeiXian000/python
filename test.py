from unittest import TestCase

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

import main


class TestCase(object):
    def __init__(self):
        self.dr = webdriver.Chrome()
        self.dr.get('http://wwww.baidu.com')
        self.dr.maximize_window()
        sleep(2)

    def test_id(self):
        #id是唯一的
        self.dr.find_element_by_id('kw').send_keys('selenium')
        self.dr.find_element_by_id('su').click()
        sleep(2)
        # self.dr.quit()

    def test_name(self):
        #find_element_by_name()方法可能返回多个元素，返回第一个
        #find_elements_by_name()是返回一个集合
        self.dr.find_element_by_name('wd').send_keys('name')
        self.dr.find_element_by_id('su').click()
        sleep(2)
        self.dr.quit()

    def test_linktest(self):
        self.test_id()
        self.dr.find_element_by_link_text('百度首页').click()
        sleep(2)
        self.dr.quit()

    def test_partial_linktext(self):
        self.test_id()
        self.dr.find_element_by_partial_link_text('首页').click()
        sleep(2)
        self.dr.quit()

    def test_xpath(self):
        self.dr.find_element_by_xpath('//*[@id="kw"]').send_keys('极客时间')
        self.dr.find_element_by_xpath('//*[@id="su"]').click()
        sleep(2)
        self.dr.quit()

    def test_tag(self):
        input = self.dr.find_element_by_tag_name('input')[0]
        print(input)

    def test_css_selector(self):
        self.dr.find_element_by_css_selector('#kw').send_keys('selenium')
        self.dr.find_element_by_css_selector('#su').click()
        sleep(2)
        self.dr.quit()

    def test_classname(self):
        self.dr.find_element_by_class_name('s_ipt').send_keys('selenium')
        self.dr.find_element_by_class_name('s_btn').click()
        sleep(2)
        self.dr.quit()

    def test_all(self):
        self.dr.find_element(value='kw').send_keys('selenium')
        self.dr.find_element(value='su').click()
        sleep(2)
        self.dr.quit()


if __name__=='__main__':
    case = TestCase()
    case.test_all()



