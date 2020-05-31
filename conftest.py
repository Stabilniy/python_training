import pytest
from fixtures.application import Application

#fixture = Application()

fixture = None
@pytest.fixture
def app(request):

    global fixture
    if fixture is None:
        browser = request.config.getoption("--browser")
        base_url = request.config.getoption("--base_url")
        fixture = Application(browser=browser, base_url=base_url)
    else:
        if not fixture.is_valid():
            browser = request.config.getoption("--browser")
            base_url = request.config.getoption("--base_url")
            fixture = Application(browser=browser, base_url=base_url)
    username = request.config.getoption("--username")
    password = request.config.getoption("--password")
    fixture.session.ensure_login(username=username, password=password)
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--base_url", action="store", default="http://localhost/addressbook/")
    parser.addoption("--username", action="store")
    parser.addoption("--password", action="store")



