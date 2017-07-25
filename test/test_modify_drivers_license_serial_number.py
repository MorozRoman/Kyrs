from model.account import Account
from model.drivers_license import DriversLicense



def test_Drop_down_menu_popular_services(app):
    app.session.login(Account(username=" ", password=" "))
    app.pages.modify_drivers_license(DriversLicense(serial_number="9999999999"))
    app.session.logout()