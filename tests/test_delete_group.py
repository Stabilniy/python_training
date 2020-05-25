# -*- coding: utf-8 -*-
from modules.group import Group
from random import randrange

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header = "testheader", footer = "testfooter"))
    old_group = app.group.get_group_list()
    index = randrange(len(old_group))
    app.group.delete_group_by_index(index)
    assert len(old_group) - 1 == app.group.count()
    new_group = app.group.get_group_list()
    old_group [index:index+1] = []
    assert old_group == new_group

