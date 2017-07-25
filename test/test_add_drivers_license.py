from model.account import Account

def test_add_drivers_license(app):
    app.session.login(Account(username=" ", password=" "))
    app.pages.add_drivers_license()
    app.session.logout()