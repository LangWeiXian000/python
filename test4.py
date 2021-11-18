from selenium import webdriver
import os
from time import sleep
class TestCase(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        path = os.path.dirname(os.path.abspath(__file__))
        file_path = 'file:///'+path+'/forms2.html'
        self.driver.get(file_path)

    def test_checkbox(self):
        self.driver.find_element_by_name('swimming').click()
        self.driver.find_element_by_name('reading').click()
        self.driver.find_element_by_xpath('/html/body/input[4]').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/input[5]').click()



if __name__ == '__main__':
    case = TestCase()
    case.test_checkbox()