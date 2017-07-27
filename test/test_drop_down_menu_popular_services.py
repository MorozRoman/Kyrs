# -*- coding: utf-8 -*-
from model.account import Account


def test_Drop_down_menu_popular_services(app):
    # app.session.login(Account(username=" ", password=" "))
    app.pages.present_popular_services()
    app.pages.go_to_pages()
    # app.session.logout()
