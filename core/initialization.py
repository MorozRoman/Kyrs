from selenium import webdriver
import time
from core.session import SessionHelper
from core.pages import PagesHelper


# По курсу папка не core, а fixture
# В данный класс переносим все вспомогательные методы
class Initialization:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.pages = PagesHelper(self)



    def open_home_page(self):
        wd = self.wd
        wd.get("https://www.mos.ru/")

    def destroy(self):
        self.wd.quit()
