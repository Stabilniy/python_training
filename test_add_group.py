# -*- coding: utf-8 -*-
from group import Group

def test_add_group(app):
    app.login(username = "admin", password = "secret")
    app.create_group(Group(name = "testname", header = "testheader", footer = "testfooter"))
    app.logout()

def test_add_empty_group(app):
    app.login(username = "admin", password = "secret")
    app.create_group(Group(name = "", header = "", footer = ""))
    app.logout()



    

