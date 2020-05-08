def test_add_group(app):
    app.session.login(username = "admin", password = "secret")
    app.contact.delete()
    app.session.logout()