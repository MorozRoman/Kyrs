from model.account import Account
from model.drivers_license import DriversLicense




def test_add_drivers_license(app):
    # app.session.login(Account(username=" ", password=" "))
    app.pages.add_drivers_license(DriversLicense(serial_number="6666666666", date_issue="28032009"))
    # app.session.logout()