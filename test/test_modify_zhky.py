
def test_modify_payment_information_apartment_description(app):
    # app.pages.modify_payment_information(DriversLicense(serial_number="9999999999"))

    old_lists=app.pages.get_lits()
    app.pages.modify_payment_information(apartment_description="вот так вот", flat_number=None)
    new_lists = app.pages.get_lits()
    assert len(old_lists) == len(new_lists)

def test_modify_payment_information_flat_number(app):

    old_lists=app.pages.get_lits()
    app.pages.modify_payment_information(apartment_description=None, flat_number="666")
    new_lists = app.pages.get_lits()
    assert len(old_lists) == len(new_lists)