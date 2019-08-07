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
        # �����˵����Ż�ȯ�һ�����ȯ /html/body/div[3]/div[1]/div/ul/li[1]/ul/li[4]/a
        elem_code2vou = driver.find_element_by_xpath('/html/body/div[3]/div[1]/div/ul/li[1]/ul/li[4]/a')
        elem_code2vou.click()
        time.sleep(1)

    def createVoucher_step1(self):
        driver = self.driver
        elem_create = driver.find_element_by_link_text('-�½�')
        elem_create.click()
        time.sleep(1)
        # �Ż���һ�����ȯ-����� ҳ��
            # �����
        elem_activename = driver.find_element_by_name('name')
        elem_activename.send_keys('test�%s'%(str(time.time())[-5:]))

            # �ʱ�䡾��ʼ��ʱ��ؼ�
        input_stime = driver.find_element_by_id('stime')
        input_stime.click()
        time.sleep(1)
                # ѡ�����ڣ�tr[x]/td[y]��ʾ���������ϵĵ�x�е�y��,ÿ�춼�仯
        sdate_xpath = "//tbody/%s/span"%(self.calendar_xpath)
        select_sdate = driver.find_element_by_xpath(sdate_xpath)
        select_sdate.click()
        time.sleep(1)
                # ѡ��ʱ��,span[x]��ʾ (x+1):00��
        sdatetime_xpath = "//tbody/tr/td/span[18]"
        select_sdatetime = driver.find_element_by_xpath(sdatetime_xpath)
        select_sdatetime.click()
        time.sleep(1)

            # �ʱ�䡾��ʼ��ʱ��ؼ�
        input_etime = driver.find_element_by_id('etime')
        input_etime.click()
        time.sleep(1)
                # ѡ�����ڣ�tr[x]/td[y]��ʾ���������ϵĵ�x�е�y��
        edate_xpath = "//tbody/%s/span"%(self.calendar_xpath)
        select_edate = driver.find_element_by_xpath(edate_xpath)
        select_edate.click()
        time.sleep(1)
                # ѡ��ʱ��,span[x]��ʾ (x+1):00��
        edatetime_xpath = "//tbody/tr/td/span[20]"
        select_edatetime = driver.find_element_by_xpath(edatetime_xpath)
        select_edatetime.click()
        time.sleep(5)
            # ���ע
        elem_activendesc = driver.find_element_by_name('desc')
        elem_activendesc.send_keys('test���ע��%s'%(str(time.time())))
        time.sleep(1)
            # ��һ��
        btn_next = driver.find_element_by_xpath('//*[@id="contentdetail"]/div[2]/div[2]/div[2]/form[1]/div[5]/button/span')
        btn_next.click()
        time.sleep(5)

    def createVoucher_step2(self):
        driver = self.driver
        # �Ż������
        input_v_num = driver.find_element_by_xpath("//*[@id=\"contentdetail\"]/div[2]/div[2]/div[2]/form[2]/div[1]/p/span/input")
        input_v_num.clear()
        input_v_num.send_keys(random.randint(1,5))
        # ����ȯ���
        input_v_amount = driver.find_element_by_xpath("//*[@id=\"contentdetail\"]/div[2]/div[2]/div[2]/form[2]/div[3]/div[2]/p/span/input[1]")
        input_v_amount.clear()
        input_v_amount.send_keys(random.randint(6,12))


        # ȯ��Чʱ��
            # �ʱ�䡾��ʼ��ʱ��ؼ�
        input_effecTime = driver.find_element_by_id('effecTime')
        input_effecTime.click()
        time.sleep(1)
                # ѡ�����ڣ�tr[x]/td[y]��ʾ���������ϵĵ�x�е�y��
        sdate_xpath = "//tbody/%s/span"%(self.calendar_xpath)
        select_sdate = driver.find_element_by_xpath(sdate_xpath)
        select_sdate.click()
        time.sleep(1)

            # �ʱ�䡾��ֹ��ʱ��ؼ�
        input_termTime = driver.find_element_by_id('termTime')
        input_termTime.click()
        time.sleep(1)
                # ѡ�����ڣ�tr[x]/td[y]��ʾ���������ϵĵ�x�е�y��
        edate_xpath = "//tbody/%s/span"%(self.calendar_xpath)
        select_edate = driver.find_element_by_xpath(edate_xpath)
        select_edate.click()
        time.sleep(1)

        # ���޴���
        radio_v_nolimit = driver.find_element_by_xpath("//input[@value='infinite']")
        radio_v_nolimit.click()
        time.sleep(1)
        input_threshold = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[2]/div[2]/form[2]/div[3]/div[4]/p/span/input")
        input_threshold.send_keys("0")
        time.sleep(1)

        # ������ҳ�����·�,Ȼ�� ������水ť
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
            print("------ִ�� %s ��"%x)
        # self.driver.quit()
if __name__ == '__main__':
    unittest.main()