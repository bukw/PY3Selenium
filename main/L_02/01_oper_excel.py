import xlrd
import unittest
import time,json
from xlutils.copy import copy
from ddt import ddt,data,file_data,unpack
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from HTMLTestRunner_my import HTMLTestRunner
class ExcelUtil(object): 
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)        
        #get titles
        self.row = self.table.row_values(0)        
        #get rows number
        self.rowNum = self.table.nrows        
        #get columns number
        self.colNum = self.table.ncols        
        #the current column
        self.curRowNo = 1
        
    def next(self):
        r = []
        while self.hasNext():
            s = {}
            col = self.table.row_values(self.curRowNo)
            i = self.colNum
            for x in range(i):
                s[self.row[x]] = col[x]
            r.append(s)
            self.curRowNo += 1
        return r       
    
    def hasNext(self):
        if self.rowNum == 0 or self.rowNum <= self.curRowNo :
            return False
        else:
            return True

excel = ExcelUtil('..\\..\\testcases\\case_01.xls', 'ok')


@ddt
class loginMerchant(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox(executable_path = "..\\..\\drivers\\geckodriver.exe")
        cls.driver.get("https://bjw.halodigit.com:9060/nereus/manager/index#/login")
        # pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        # pass

        
    # 关键在于获取所有excel数据
    @data(*excel.next())
    def test_Login(self,case):
        name, pwd, xpath, asserttext = case['name'],case['pwd'],case['xpath'],case['asserttext']
        print(name, pwd, xpath, asserttext)
        driver = self.driver
        name_elem = driver.find_element_by_id("loginName")
        name_elem.clear()
        time.sleep(1)
        name_elem.send_keys(name)
        pwd_elem = driver.find_element_by_id("loginPwd")
        pwd_elem.clear()
        time.sleep(1)
        pwd_elem.send_keys(pwd)
        pwd_elem.send_keys(Keys.RETURN)
        time.sleep(2)
        try:
            msg_wrongpwd = driver.find_element_by_xpath(xpath)
            self.assertEqual(msg_wrongpwd.text, asserttext)
            time.sleep(2)
        except  Exception as e:
            raise e

if __name__ == '__main__':
    # unittest.main()


    mySuite = unittest.TestSuite()
    mySuite.addTest(unittest.makeSuite(loginMerchant))

    filename = './myreports/report.html'
    fp = open(filename, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(
        stream=fp,
        title=u'商户后台登录 自动化测试_测试报告',
        description=u'用例执行情况：',
        verbosity=2)  # verbosity=2,输出测试用例中打印的信息
    runner.run(mySuite)
    fp.close()