

def test_add_payment_information(app):

    old_lists=app.pages.get_lits()
    app.pages.add_payment_information(apartment_description = "что-то", flat_number = "77")
    new_lists = app.pages.get_lits()
    assert len(old_lists) + 1 == len(new_lists)



