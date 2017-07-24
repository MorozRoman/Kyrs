# -*- coding: utf-8 -*-
import unittest
import pytest
import time
from selenium import webdriver



class test_drop_down_menu_popular_services(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)

    def logout(self, wd):
        # logout mos.ru
        time.sleep(2)
        wd.find_element_by_class_name('mos-layout-icon-dropdown_up').click()
        wd.find_element_by_class_name("mos-layout-auth-out").click()

    def go_to_pages(self, wd):
        # Проверка страниц
        # переход к 1
        # wd.find_elements_by_xpath('//div[contains(@class, "mos-layouts-services_menu-popular")]/ul/li/a')[1].click()
        # time.sleep(2)
        wd.find_element_by_link_text("Результаты поквартирного голосования по проекту программы реновации").click()
        # wd.find_element_by_css_selector("h1")
        time.sleep(2)
        # переход к 2
        wd.find_element_by_link_text("Приём показаний приборов учёта воды").click()
        # wd.find_element_by_css_selector("h1")
        time.sleep(2)
        # переход к 3
        wd.find_element_by_link_text("Получить и оплатить единый платежный документ (ЕПД)").click()
        # wd.find_element_by_css_selector("h1")
        time.sleep(2)
        # переход к 4
        wd.find_element_by_link_text("Поиск и оплата штрафов").click()
        wd.find_element_by_css_selector("h1")
        time.sleep(2)
        # переход к 5
        wd.find_element_by_link_text("Запись на приём к врачу, отмена и перенос записи").click()
        wd.find_element_by_css_selector("h1")
        time.sleep(2)

    def present_popular_services(self, wd):
        # Проверка на наличия 5 популярных услуг в верхнем выпадающем меню
        wd.find_element_by_class_name('mos-layouts-services_menu-popular')
        self.assertEqual(
            len(wd.find_elements_by_xpath('//div[contains(@class, "mos-layouts-services_menu-popular")]/ul/li/a')), 6)

    def login(self, wd, username, password):
        # login
        wd.find_element_by_class_name("mos-header__controls-login-button-enter").click()
        wd.find_element_by_id("alias").click()
        wd.find_element_by_id("alias").clear()
        wd.find_element_by_id("alias").send_keys(username)
        # password
        wd.find_element_by_id("aliaspswd").click()
        wd.find_element_by_id("aliaspswd").clear()
        wd.find_element_by_id("aliaspswd").send_keys(password)
        wd.find_element_by_id('outerlogin_button').click()

    def open_home_page(self, wd):
        wd.get("https://www.mos.ru/")


    def test_Drop_down_menu_popular_services(self):

        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, " ", " ")
        self.present_popular_services(wd)
        self.go_to_pages(wd)
        self.logout(wd)




    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
