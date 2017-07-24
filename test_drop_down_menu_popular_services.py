# -*- coding: utf-8 -*-
from account import Account
import pytest
from initialization import Initialization

# Функция создающая фикстуру
# requset.addfinalizer - параметр с методом разрушающий фикстуру
@pytest.fixture()
def app(request):
    fixture = Initialization()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_Drop_down_menu_popular_services(app):
    app.login(Account(username=" ", password=" "))
    app.present_popular_services()
    app.go_to_pages()
    app.logout()
