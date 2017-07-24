# -*- coding: utf-8 -*-
import pytest

from core.initialization import Initialization
from model.account import Account


# Функция создающая фикстуру
# requset.addfinalizer - параметр с методом разрушающий фикстуру
@pytest.fixture()
def app(request):
    fixture = Initialization()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_Drop_down_menu_popular_services(app):
    app.session.login(Account(username=" ", password=" "))
    app.pages.present_popular_services()
    app.pages.go_to_pages()
    app.session.logout()
