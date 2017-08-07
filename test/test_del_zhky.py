

def test_add_payment_information(app):

    old_lists=app.pages.get_lits()
    app.pages.del_payment_information()
    new_lists = app.pages.get_lits()
    assert len(old_lists) - 1 == len(new_lists)
    app.scroll_to_up()
    # Это в данный момент неработает, так как нет привязки к индивидуальному идентификатору типа id
    # old_lists[0:1]=[]
    # assert old_lists==new_lists