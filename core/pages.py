import time

class PagesHelper:
    def  __init__(self, app):
        self.app = app

    def go_to_pages(self):
        wd = self.app
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

    def present_popular_services(self):
        wd = self.app.wd
        # Проверка на наличия 5 популярных услуг в верхнем выпадающем меню
        wd.find_element_by_class_name('mos-layouts-services_menu-popular')
        count = len(wd.find_elements_by_xpath(
            '//div[contains(@class, "mos-layouts-services_menu-popular")]/ul/li/a[@target="_self"]'))
        assert True == (count == 5)
        # self.assertEqual(len(wd.find_elements_by_xpath('//div[contains(@class, "mos-layouts-services_menu-popular")]/ul/li/a')),6)
