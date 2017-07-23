# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from waiting import wait


class Drop_down_menu_popular_services(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
    
    def test_Drop_down_menu_popular_services(self):

        wd = self.wd
        wd.get("https://www.mos.ru/")
        wd.assertEquel('mos-layouts-services_menu-popular')
        wd.find_element_by_link_text("Результаты поквартирного голосования по проекту программы реновации").click()

        wd.find_element_by_css_selector("h1").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
