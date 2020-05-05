# -*- coding: utf-8 -*-
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group
from Application import Application

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    #wd = app.wd
    app.login(username = "admin", password = "secret")
    app.create_group(Group(name = "testname", header = "testheader", footer = "testfooter"))
    app.logout()

def test_add_empty_group(app):
    #wd = app.wd
    app.login(username = "admin", password = "secret")
    app.create_group(Group(name = "", header = "", footer = ""))
    app.logout()



    

