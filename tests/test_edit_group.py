# -*- coding: utf-8 -*-
from modules.group import Group

def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header="testheader", footer="testfooter"))
    old_group = app.group.get_group_list()
    group = Group(name = "_test_to_check_edit222", header = "_test_to_check_edit222", footer = "_test_to_check_edit222")
    group.id = old_group[0].id
    app.group.edit(group)
    assert len(old_group) == app.group.count()
    new_group = app.group.get_group_list()
    old_group[0] = group
    assert sorted(old_group, key=Group.id_or_max) == sorted(new_group, key=Group.id_or_max)

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header="testheader", footer="testfooter"))
    old_group = app.group.get_group_list()
    app.group.edit(Group(name = "NAME!!!!!!!!!!!!!!"))
    assert len(old_group) == app.group.count()
    #new_group = app.group.get_group_list()


def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header="testheader", footer="testfooter"))
    old_group = app.group.get_group_list()
    app.group.edit(Group(header = "HEADER!!!!!!!!!!"))
    assert len(old_group) == app.group.count()
    new_group = app.group.get_group_list()


def test_edit_group_footer(app):
    old_group = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header="testheader", footer="testfooter"))
    app.group.edit(Group(footer = "FOOTER!!!!!!!!!!"))
    assert len(old_group) == app.group.count()
    new_group = app.group.get_group_list()
