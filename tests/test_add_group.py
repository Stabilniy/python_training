# -*- coding: utf-8 -*-
from modules.group import Group

import time

def test_add_group(app):
    app.group.create_group(Group(name = "testname", header = "testheader", footer = "testfooter"))


def test_add_empty_group(app):
    app.group.create_group(Group(name = "", header = "", footer = ""))

def test_add_group_name(app):
    app.group.create_group(Group(name = "NAME!!!!!"))

def test_add_group_header(app):
    app.group.create_group(Group(header = "HEADER!!!!!!"))

def test_add_group_footer(app):
    app.group.create_group(Group(footer = "FOOTER!!!!"))





    

