# -*- coding: utf-8 -*-
from modules.group import Group

import time

def test_add_group(app):
    old_group = app.group.get_group_list()
    group = (Group(name="testname", header="testheader", footer="testfooter"))
    app.group.create_group(group)
    new_group = app.group.get_group_list()
    assert len(old_group) +1 == len(new_group)
    old_group.append(group)
    assert sorted(old_group, key =Group.id_or_max) == sorted(new_group, key=Group.id_or_max)

print ("OK")
'''
def test_add_empty_group(app):
    old_group = app.group.get_group_list()
    group = Group(name = "", header = "", footer = "")
    app.group.create_group(group)
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


def test_add_group_name(app):
    old_group = app.group.get_group_list()
    group = Group(name = "NAME!!!!!")
    app.group.create_group(group)
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


#def test_add_group_header(app):
#    old_group = app.group.get_group_list()
#    group = Group(header = "HEADER!!!!!!")
#    app.group.create_group(group)
#    new_group = app.group.get_group_list()
#    assert len(old_group) + 1 == len(new_group)
#    old_group.append(group)
#    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)


def test_add_group_footer(app):
    old_group = app.group.get_group_list()
    group = Group(footer = "FOOTER!!!!")
    app.group.create_group(group)
    new_group = app.group.get_group_list()
    assert len(old_group) + 1 == len(new_group)
    old_group.append(group)
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)

'''




    

