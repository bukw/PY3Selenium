import unittest
import time
from ddt import ddt,data,unpack
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

    case = (('85558888','a666666','''//*[@id="login-holder"]/div[4]/form/div/div[2]/div[4]/p''','Incorrect account or password'),
            ('855','a111111','''/html/body/div[1]/div[4]/form/div/div[2]/em[1]''','The length cannot be less than10'),
            ('81234567890123456','a111111','''/html/body/div[1]/div[4]/form/div/div[2]/em[1]''','The length cannot be more than15')
            )
    case2 = ((1, 2))
    @data(case2)
    # @unpack
    def test_something(self, case2):
        value1, value2 = case2
        print(value1, value2)
        self.assertEqual(value2, value1 + 1)

    @data(*case)
    # @unpack
    def test_namelen_less10(self,case):
        name, pwd, xpath, asserttext = case
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

if __name__ == "__main__":
    unittest.main()