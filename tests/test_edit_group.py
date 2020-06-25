# -*- coding: utf-8 -*-
from modules.group import Group
import random

def test_edit_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header="testheader", footer="testfooter"))
    old_group = db.get_group_list()
    group = Group(name = "_test_to_check_edit222", header = "_test_to_check_edit222", footer = "_test_to_check_edit222")
    group_random = random.choice(old_group)
    app.group.edit_group_by_id(group, group_random.id)
    assert len(old_group) == app.group.count()
    new_group = db.get_group_list()
    if (check_ui):
        assert sorted(new_group, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)
