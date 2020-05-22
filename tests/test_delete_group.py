# -*- coding: utf-8 -*-
from modules.group import Group
def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header = "testheader", footer = "testfooter"))
    old_group = app.group.get_group_list()
    app.group.delete()
    assert len(old_group) - 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group [0:1] = []
    assert old_group == new_group

