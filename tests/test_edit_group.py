# -*- coding: utf-8 -*-
from modules.group import Group

def test_add_group(app):
    app.group.edit(Group(name = "_test_to_check_edit222", header = "_test_to_check_edit222", footer = "_test_to_check_edit222"))