# -*- coding: utf-8 -*-
from modules.group import Group

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_group = db.get_group_list()
    app.group.create_group(group)
    new_group = db.get_group_list()
    old_group.append(group)
    assert sorted(old_group, key =Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
    if (check_ui):
        assert sorted(new_group, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)
    print(old_group)



    

