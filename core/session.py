



class SessionHelper:

    def  __init__(self, app):
        self.app = app

    def login(self, account):
        wd = self.app.wd
        self.app.open_home_page()
        # login
        wd.find_element_by_class_name("mos-header__controls-login-button-enter").click()
        wd.find_element_by_id("alias").click()
        wd.find_element_by_id("alias").clear()
        wd.find_element_by_id("alias").send_keys(account.username)
        # password
        wd.find_element_by_id("aliaspswd").click()
        wd.find_element_by_id("aliaspswd").clear()
        wd.find_element_by_id("aliaspswd").send_keys(account.password)
        wd.find_element_by_id('outerlogin_button').click()

    def logout(self):
        wd = self.app.wd
        # logout mos.ru
        # time.sleep(2)
        wd.find_element_by_class_name('mos-layout-icon-dropdown_up').click()
        wd.find_element_by_class_name("mos-layout-auth-out").click()

