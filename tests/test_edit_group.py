# -*- coding: utf-8 -*-
from modules.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header="testheader", footer="testfooter"))
    app.group.edit(Group(name = "_test_to_check_edit222", header = "_test_to_check_edit222", footer = "_test_to_check_edit222"))

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header="testheader", footer="testfooter"))
    app.group.edit(Group(name = "NAME!!!!!!!!!!!!!!"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header="testheader", footer="testfooter"))
    app.group.edit(Group(header = "HEADER!!!!!!!!!!"))

def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header="testheader", footer="testfooter"))
    app.group.edit(Group(footer = "FOOTER!!!!!!!!!!"))
