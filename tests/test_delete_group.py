# -*- coding: utf-8 -*-
from modules.group import Group
def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header = "testheader", footer = "testfooter"))
    app.group.delete()