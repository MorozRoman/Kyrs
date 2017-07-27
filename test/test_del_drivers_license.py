from model.drivers_license import DriversLicense


def test_del_drivers_license(app):
    if app.pages.count() == 0:
        app.pages.add_drivers_license(DriversLicense(serial_number="4444444444", date_issue="28032009"))
    app.pages.delete_drivers_license()

# Выполнение предусловий, это зона ответственности тестов