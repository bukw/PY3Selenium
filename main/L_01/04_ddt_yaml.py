import unittest
import time,json,yaml
from ddt import ddt,data,file_data,unpack
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@ddt
class LoginMerchant(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # cls.driver = webdriver.Firefox(executable_path = "..\\..\\drivers\\geckodriver.exe")
        # cls.driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")
        pass

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def setUp(self):
        pass
    def tearDown(self):
        pass

    # @unpack
    @file_data('..\\..\\testcases\\case03.yaml')
    def test_something(self,kwargs):
        # pass
        # kwargs = json.load(kwargs)
        print(kwargs, type(kwargs))
        # print(kwargs('name'))
        # name = kwargs.get("name")
        # pwd = kwargs.get("pwd")
        # xpath = kwargs.get("xpath")
        # asserttext = kwargs.get('asserttext')
        # print(name,pwd,xpath)

    # @data(*case)
    # # @unpack
    # def test_namelen_less10(self,case):
    #     name, pwd, xpath, asserttext = case
    #     driver = self.driver
    #     name_elem = driver.find_element_by_id("loginName")
    #     name_elem.clear()
    #     time.sleep(1)
    #     name_elem.send_keys(name)
    #     pwd_elem = driver.find_element_by_id("loginPwd")
    #     pwd_elem.clear()
    #     time.sleep(1)
    #     pwd_elem.send_keys(pwd)
    #     pwd_elem.send_keys(Keys.RETURN)
    #     time.sleep(2)
    #     try:
    #         msg_wrongpwd = driver.find_element_by_xpath(xpath)
    #         self.assertEqual(msg_wrongpwd.text, asserttext)
    #         time.sleep(2)
    #     except  Exception as e:
    #         raise e

if __name__ == "__main__":
    unittest.main()