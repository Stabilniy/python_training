from modules.group import Group

def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.group.edit(Group(name = "_test_to_check_edit", header = "_test_to_check_edit", footer = "_test_to_check_edit"))
    app.session.logout()