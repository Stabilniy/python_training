# -*- coding: utf-8 -*-
def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.delete()
    app.session.logout()