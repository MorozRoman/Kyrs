# -*- coding: utf-8 -*-
import unittest

import time
from selenium import webdriver



class test_drop_down_menu_popular_services(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)
    
    def test_Drop_down_menu_popular_services(self):

        wd = self.wd
        wd.get("https://www.mos.ru/")
        # wd.('mos-layouts-services_menu-popular')
        # if wd.find_element_by_class_name('mos-layouts-services_menu-popular'):
        #
        # else:
        #     return print("Not Found")
        # Log in mos.ru
        wd.find_element_by_class_name("mos-header__controls-login-button-enter").click()
        wd.find_element_by_id("alias").click()
        wd.find_element_by_id("alias").clear()
        wd.find_element_by_id("alias").send_keys(" ")
        wd.find_element_by_id("aliaspswd").click()
        wd.find_element_by_id("aliaspswd").clear()
        wd.find_element_by_id("aliaspswd").send_keys(" ")
        wd.find_element_by_id('outerlogin_button').click()
        # wd.find_element_by_link_text("Результаты поквартирного голосования по проекту программы реновации").click()
        # wd.find_element_by_css_selector("h1").click()

        # log out mos.ru
        time.sleep(2)
        wd.find_element_by_class_name('mos-layout-icon-dropdown_up').click()
        wd.find_element_by_class_name("mos-layout-auth-out").click()



    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
