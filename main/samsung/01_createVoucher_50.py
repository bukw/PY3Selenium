# -*- coding: gb2312 -*- 
import time,random
import unittest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class loginMerchant(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        td = datetime.now()
        month_week = int(datetime(td.year, td.month, td.day).strftime("%W")) - int(datetime(td.year, td.month,1).strftime("%W")) +1
        week_day = td.strftime("%w")
        cls.calendar_xpath = "tr[%s]/td[%s]"%(month_week,week_day)
        cls.driver = webdriver.Firefox(executable_path = "..\\..\\drivers\\geckodriver.exe")
        cls.driver.get("http://samsung.halodigit.com:8002/mkt/admin/index#/login")
        cls.driver.maximize_window()
        cls.loginname = "admin@iapppay.com"
        cls.pwd = "123456"
        cls.loginSuccess()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        pass
    def tearDown(self):
        pass
    @classmethod
    def loginSuccess(self):
        driver = self.driver
        # with open('./login.yaml') as f:
            # login = yaml.load(f)
        # loginname = login["successLogin"]["loginname"]
        # pwd = login["successLogin"]["pwd"]
        name_elem = driver.find_element_by_id("loginName")
        name_elem.clear()
        time.sleep(1)
        name_elem.send_keys(self.loginname)
        pwd_elem = driver.find_element_by_id("loginPwd")
        pwd_elem.clear()
        time.sleep(1)
        pwd_elem.send_keys(self.pwd)
        pwd_elem.send_keys(Keys.RETURN)
        time.sleep(2)
        # 二级菜单，优惠券兑换代金券 /html/body/div[3]/div[1]/div/ul/li[1]/ul/li[4]/a
        elem_code2vou = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/ul/li[1]/ul/li[4]/a')
        elem_code2vou.click()
        time.sleep(1)

    def createVoucher_step1(self):
        driver = self.driver
        elem_create = driver.find_element_by_link_text('-新建')
        elem_create.click()
        time.sleep(1)
        # 优惠码兑换代金券-创建活动 页面
            # 活动名称
        elem_activename = driver.find_element_by_name('name')
        elem_activename.send_keys('test活动%s'%(str(time.time())[-5:]))

            # 活动时间【开始】时间控件
        input_stime = driver.find_element_by_id('stime')
        input_stime.click()
        time.sleep(1)
                # 选择日期，tr[x]/td[y]表示日期日历上的第x行第y列,每天都变化
        sdate_xpath = "//tbody/%s/span"%(self.calendar_xpath)
        select_sdate = driver.find_element_by_xpath(sdate_xpath)
        select_sdate.click()
        time.sleep(1)
                # 选择时间,span[x]表示 (x+1):00点
        sdatetime_xpath = "//tbody/tr/td/span[18]"
        select_sdatetime = driver.find_element_by_xpath(sdatetime_xpath)
        select_sdatetime.click()
        time.sleep(1)

            # 活动时间【开始】时间控件
        input_etime = driver.find_element_by_id('etime')
        input_etime.click()
        time.sleep(1)
                # 选择日期，tr[x]/td[y]表示日期日历上的第x行第y列
        edate_xpath = "//tbody/%s/span"%(self.calendar_xpath)
        select_edate = driver.find_element_by_xpath(edate_xpath)
        select_edate.click()
        time.sleep(1)
                # 选择时间,span[x]表示 (x+1):00点
        edatetime_xpath = "//tbody/tr/td/span[20]"
        select_edatetime = driver.find_element_by_xpath(edatetime_xpath)
        select_edatetime.click()
        time.sleep(5)
            # 活动备注
        elem_activendesc = driver.find_element_by_name('desc')
        elem_activendesc.send_keys('test活动备注：%s'%(str(time.time())))
        time.sleep(1)
            # 下一步
        btn_next = driver.find_element_by_xpath('//*[@id="contentdetail"]/div[2]/div[2]/div[2]/form[1]/div[5]/button/span')
        btn_next.click()
        time.sleep(5)

    def createVoucher_step2(self):
        driver = self.driver
        # 优惠码个数
        input_v_num = driver.find_element_by_xpath("//*[@id=\"contentdetail\"]/div[2]/div[2]/div[2]/form[2]/div[1]/p/span/input")
        input_v_num.clear()
        input_v_num.send_keys(random.randint(1,5))
        # 代金券面额
        input_v_amount = driver.find_element_by_xpath("//*[@id=\"contentdetail\"]/div[2]/div[2]/div[2]/form[2]/div[3]/div[2]/p/span/input[1]")
        input_v_amount.clear()
        input_v_amount.send_keys(random.randint(6,12))


        # 券有效时间
            # 活动时间【开始】时间控件
        input_effecTime = driver.find_element_by_id('effecTime')
        input_effecTime.click()
        time.sleep(1)
                # 选择日期，tr[x]/td[y]表示日期日历上的第x行第y列
        sdate_xpath = "//tbody/%s/span"%(self.calendar_xpath)
        select_sdate = driver.find_element_by_xpath(sdate_xpath)
        select_sdate.click()
        time.sleep(1)

            # 活动时间【截止】时间控件
        input_termTime = driver.find_element_by_id('termTime')
        input_termTime.click()
        time.sleep(1)
                # 选择日期，tr[x]/td[y]表示日期日历上的第x行第y列
        edate_xpath = "//tbody/%s/span"%(self.calendar_xpath)
        select_edate = driver.find_element_by_xpath(edate_xpath)
        select_edate.click()
        time.sleep(1)

        # 不限次数
        radio_v_nolimit = driver.find_element_by_xpath("//input[@value='infinite']")
        radio_v_nolimit.click()
        time.sleep(1)
        input_threshold = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/form[2]/div[3]/div[4]/p/span/input")
        input_threshold.send_keys("0")
        time.sleep(1)

        # 下拉到页面最下方,然后 点击保存按钮
        btn_save = driver.find_element_by_id("subBtn")
        time.sleep(1)
        driver.execute_script("arguments[0].scrollIntoView();", btn_save)
        time.sleep(1)
        btn_save.click()
        time.sleep(2)

    def test_cycle_50(self):
        for x in range(1,51):
            self.createVoucher_step1()
            self.createVoucher_step2()
            print("------执行 %s 次"%x)
        # self.driver.quit()
if __name__ == '__main__':
    unittest.main()