import time

from model.drivers_license import DriversLicense


class PagesHelper:
    def  __init__(self, app):
        self.app = app

    def go_to_pages(self):
        wd = self.app
        # Проверка страниц
        # переход к 1

        # wd.find_element_by_xpath('//*[@id="mos-header"]/div[1]/div/div[2]/div[1]/div/div/div[1]/div[1]/ul[2]/li[1]').click()
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
        count = len(wd.find_elements_by_xpath('//div[contains(@class, "mos-layouts-services_menu-popular")]/ul/li/a[@target="_self"]'))
        assert True == (count == 5)
        # self.assertEqual(len(wd.find_elements_by_xpath('//div[contains(@class, "mos-layouts-services_menu-popular")]/ul/li/a')),6)


    def add_drivers_license(self, drivers_license):
        wd = self.app.wd
        # self.go_to_profil()
        self.go_to_profile()
        wd.switch_to_window(wd.window_handles[1])
        # wd.find_element_by_link_text('+ Водительское удостоверение')
        if (wd.find_element_by_xpath('//*[@data-link="DRIVER_LICENSE"]/div/div/div/div/h2/a[@class="view-link"]')):
            self.remove_driver_license()
        wd.find_element_by_link_text("+ Водительское удостоверение").click()
        self.fill_drivers_license_form(drivers_license)


    def go_to_profile(self):
        wd = self.app.wd
        # Оптимизация переходов между страницами
        wd.implicitly_wait(15)
        time.sleep(2)
        if not (wd.current_url.endswith('/#profile')):
            wd.find_element_by_class_name('mos-layout-icon-dropdown_up').click()
            wd.find_element_by_link_text("Личные данные").click()
        # Равносильно
        # if wd.current_url.endswith('/my/#profile'):
        #     return
        # wd.find_element_by_class_name('mos-layout-icon-dropdown_up').click()
        # wd.find_element_by_link_text("Профиль").click()

    def go_to_profil(self):
        wd = self.app.wd
        # Оптимизация переходов между страницами
        if not (wd.current_url.endswith('/my/')):
            wd.find_element_by_class_name('mos-layout-icon-dropdown_up').click()
            wd.find_element_by_link_text("Профиль").click()

    def fill_drivers_license_form(self, drivers_license):
        wd = self.app.wd
        self.input_text("input-text", drivers_license.serial_number)
        self.input_text("hasDatepicker", drivers_license.date_issue)
        wd.find_element_by_class_name('btn-save').click()
        if not wd.find_element_by_class_name('popup_messagebox'):
            wd.find_element_by_class_name('btn-subscr-save').click()
        wd.find_element_by_class_name('btn-left').click()
        wd.find_element_by_xpath('//*[@id="all-docs"]/div[1]/div[4]/div/div/div/div/a[1]').click()

    def input_text(self, field_text, text):
        wd = self.app.wd
        # Конструкция if then else:
        if text is not None:
            wd.find_element_by_class_name(field_text).click()
            wd.find_element_by_class_name(field_text).clear()
            wd.find_element_by_class_name(field_text).send_keys(text)

    # new_drivers_date
    def modify_drivers_license(self, new_drivers_date):
        wd = self.app.wd
        self.go_to_profile()
        wd.switch_to_window(wd.window_handles[1])
        wd.find_element_by_xpath('//*[@id="all-docs"]/div[1]/div[4]/div/div/div/div/a[1]').click()
        self.fill_drivers_license_form(new_drivers_date)


    def delete_drivers_license(self):
        wd = self.app.wd
        wd.switch_to_window(wd.window_handles[1])
        self.go_to_profile()
        self.remove_driver_license()

    def remove_driver_license(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="all-docs"]/div[1]/div[4]/div/div/div/div/a[2]').click()
        wd.find_element_by_class_name('btn-close-box').click()


    #Проверка на наличие элемента, если не оди, то делаем подсчет элементов
    def count(self):
        wd = self.app.wd
        self.go_to_profile()
        time.sleep(3)
        # return len(wd.find_element_by_link_text("Водительское удостоверение"))
        return 1
        # if not (wd.find_element_by_xpath('//*[@id="all-docs"]/div[1]/div[4]/div/div/div/div/h2/a')):
        #         return 0
        # return 1




