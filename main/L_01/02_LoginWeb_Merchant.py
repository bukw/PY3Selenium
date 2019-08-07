import unittest
import time
from selenium import webdriver

from selenium.webdriver.common.keys import Keys
class LoginMerchant(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Firefox(executable_path = "..\\..\\drivers\\geckodriver.exe")
		cls.driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	def setUp(self):
		pass
	def tearDown(self):
		pass

	def test_wrong_pwd(self):
		driver = self.driver
		# driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")
		self.assertIn("QRindo Merchant", driver.title)
		name_elem = driver.find_element_by_id("loginName")
		name_elem.clear()
		time.sleep(1)
		name_elem.send_keys("85558888")
		pwd_elem = driver.find_element_by_id("loginPwd")
		pwd_elem.click()
		pwd_elem.send_keys("a666666")
		pwd_elem.send_keys(Keys.RETURN)
		time.sleep(2)
		try:
			msg_wrongpwd = driver.find_element_by_xpath('//*[@id="login-holder"]/div[4]/form/div/div[2]/div[4]/p')
			self.assertEqual(msg_wrongpwd.text, 'Incorrect account or password', '用户名密码错误')
			time.sleep(2)
		except  Exception as e:
			raise e

	def test_namelen_less10(self):
		driver = self.driver
		self.assertIn("QRindo Merchant", driver.title)
		name_elem = driver.find_element_by_id("loginName")
		name_elem.clear()
		time.sleep(1)
		name_elem.send_keys("855")
		pwd_elem = driver.find_element_by_id("loginPwd")
		pwd_elem.click()
		time.sleep(2)
		# 获取提示信息'The length cannot be less than10'控件
		msg_nameless10_elem = driver.find_element_by_xpath("/html/body/div[1]/div[4]/form/div/div[2]/em[1]")
		self.assertEqual(msg_nameless10_elem.text,'The length cannot be less than10','用户名长度小于10个字母的提示信息')
		time.sleep(2)

	def test_namelen_more15(self):
		driver = self.driver
		# driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")
		self.assertIn("QRindo Merchant", driver.title)
		name_elem = driver.find_element_by_id("loginName")
		name_elem.clear()
		time.sleep(1)
		name_elem.send_keys("81234567890123456")
		pwd_elem = driver.find_element_by_id("loginPwd")
		pwd_elem.click()
		time.sleep(2)
		# 获取提示信息'The length cannot be less than10'控件
		msg_namemore15_elem = driver.find_element_by_xpath("/html/body/div[1]/div[4]/form/div/div[2]/em[1]")
		self.assertEqual(msg_namemore15_elem.text, 'The length cannot be more than15','用户名长度不能大于15个字母')
		time.sleep(2)

	def test_login_success(self):
		driver = self.driver
		# driver.get("https://bjw.halodigit.com:9060/nereus/merchant/index#/login")
		self.assertIn("QRindo Merchant", driver.title)
		name_elem = driver.find_element_by_id("loginName")
		name_elem.clear()
		time.sleep(1)
		name_elem.send_keys("85558888")
		pwd_elem = driver.find_element_by_id("loginPwd")
		pwd_elem.clear()
		time.sleep(1)
		pwd_elem.send_keys("a111111")
		pwd_elem.send_keys(Keys.RETURN)
		time.sleep(6)
		self.assertIn("Search", driver.page_source)
		account = driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/span[2]')
		account.click()
		time.sleep(1)
		logout = driver.find_element_by_xpath('//*[@id="content"]/div/div[4]/ul/li[2]/a')
		logout.click()

	def suite(self):
		suite = unittest.TestSuite()
		tests = ['test_namelen_less10', 'test_namelen_more15', 'test_login_success', 'test_wrong_pwd']
		return unittest.TestSuite(map(LoginMerchant, tests))

if __name__ == "__main__":
    suite = LoginMerchant().suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)