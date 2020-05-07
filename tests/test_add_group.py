# -*- coding: utf-8 -*-
from modules.group import Group

def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.create_group(Group(name = "testname", header = "testheader", footer = "testfooter"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.create_group(Group(name = "", header = "", footer = ""))
    app.session.logout()



    

