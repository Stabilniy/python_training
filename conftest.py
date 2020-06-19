import pytest
from fixtures.application import Application
import json
import os.path
import importlib
import jsonpickle
from fixtures.db import DbFixture

fixture = None
target = None

def load_config(file):
    global target
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
    if target is None:
        with open(config_file) as f:
            target = json.load(f)
    return target

@pytest.fixture
def app(request):
    global fixture
    #global target
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['base_url'])
    fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            tesdata = load_form_module(fixture[5:])
            metafunc.parametrize(fixture, tesdata, ids=[str(x) for x in tesdata])
        elif fixture.startswith("json_"):
            tesdata = load_form_json(fixture[5:])
            metafunc.parametrize(fixture, tesdata, ids=[str(x) for x in tesdata])

def load_form_module(module):
    return importlib.import_module("data.%s" % module).testdata

def load_form_json(file):
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/%s.json" % file)) as f:
        return jsonpickle.decode(f.read())




