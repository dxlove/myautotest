#!-*- coding:utf-8 -*-
'''
Created on 2014-11-16
@description:selenium2 webdriver API code
@author: Administrator
'''
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest,time,re,os,time

#导入公共的类
from package import common

class Baidu(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')
        self.driver=webdriver.Chrome(chrome_options=options)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.base_url=''
        self.verificationErrors=[]
        self.accept_next_alert=True


    def tearDown(self):
        driver=self.driver
        driver.close()
        self.assertEqual([],self.verificationErrors)

if __name__=='__main__':
    unittest.main()






