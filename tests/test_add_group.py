# -*- coding: utf-8 -*-
from modules.group import Group
import allure

def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step('Given a group list'):
        old_group = db.get_group_list()
    with allure.step('When I add group %s to the list' % group):
        app.group.create_group(group)
    with allure.step('Then the new group list is equal to the old list with added group'):
        new_group = db.get_group_list()
        old_group.append(group)
        assert sorted(old_group, key =Group.id_or_max) == sorted(new_group, key=Group.id_or_max)
        if (check_ui):
            assert sorted(new_group, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)
            print(old_group)



    

