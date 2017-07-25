import pytest
from core.initialization import Initialization

# Функция создающая фикстуру
# requset.addfinalizer - параметр с методом разрушающий фикстуру

@pytest.fixture(scope = "session")
def app(request):
    fixture = Initialization()
    request.addfinalizer(fixture.destroy)
    return fixture
