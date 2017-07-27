from model.account import Account
from model.drivers_license import DriversLicense



def test_modify_drivers_license_serial_number(app):
    app.session.login(Account(username=" ", password=" "))
    app.pages.modify_drivers_license(DriversLicense(serial_number="9999999999"))
    app.session.logout()

def test_modify_drivers_license_serial_date(app):
    app.session.login(Account(username=" ", password=" "))
    app.pages.modify_drivers_license(DriversLicense(date_issue="06062016"))
    app.session.logout()