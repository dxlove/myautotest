#!-*- coding:utf-8 -*-
import unittest
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''断言的测试应用'''
from selenium import webdriver


class Assertions(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        #options.add_argument('lang=zh_CN.UTF-8')
        options.add_argument("user-data-dir=C:/Users/user_name/AppData/Local/Google/Chrome/User Data")
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        #options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
        self.driver = webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url='http://www.baidu.com'
        #脚本运行时，错误的信息将打印到这个列表中
        self.verificationErrors=[]
        #是否接受下一个A警告
        self.accept_next_alert=True

    def testAssertion(self):
        '''断言的测试'''
        driver=self.driver
        driver.get(self.base_url+'/')
        #断言来判断title是否正确
        try:
            self.assertEqual(u'百度一下，你就知道',driver.title)
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    '''测试错误的截图'''
    def testImage(self):
        '''错误截图的获取'''
        driver=self.driver
        driver.get('http://www.baidu.com')
        try:
            driver.find_element_by_id('kw1ffg').send_keys('webdriver')
        except:
            driver.get_screenshot_as_file('..//image//error_png.png')


    def tearDown(self):
        driver=self.driver
        driver.close()
        self.assertEqual([],self.verificationErrors)

if __name__=='__main__':
    #创建测试容器
    suite=unittest.TestSuite()
    #添加测试用例
    suite.addTest(Assertions('testAssertion'))
    #suite.addTest(Assertions('testImage'))
    #unittest.makeSuite(Assertions,'test_case')
    #执行测试用例
    runner=unittest.TextTestRunner()
    #执行用例
    runner.run(suite)




