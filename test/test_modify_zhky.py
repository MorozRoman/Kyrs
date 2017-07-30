


def test_modify_payment_information_apartment_description(app):
    # app.pages.modify_payment_information(DriversLicense(serial_number="9999999999"))
    app.pages.modify_payment_information(apartment_description="вот так вот", flat_number=None)


def test_modify_payment_information_flat_number(app):

    app.pages.modify_payment_information(apartment_description=None,flat_number="666")


