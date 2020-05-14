# -*- coding: utf-8 -*-
from modules.contact import Contact

def test_edit_contact(app):
    app.contact.edit_contact(Contact(firstname="test_by_check_edit", middlename = "test_by_check_edit", lastname = "test_by_check_edit", nickname = "test_by_check_edit", title = "test_by_check_edit", company = "test_by_check_edit", address = "test_by_check_edit", home = "test_by_check_edit", mobile = "test_by_check_edit",
                                              work = "test_by_check_edit", fax ="test_by_check_edit", email = "test_by_check_edit", email1 = "test_by_check_edit", email2 = "test_by_check_edit", email3 = "test_by_check_edit", address2 = "test_by_check_edit", homepage = "test_by_check_edit", bday = "5", bmounth = "July",
                                              byear = "1982", aday = "2", amounth = "July", ayear = "2003", phone2 = "test_by_check_edit", notes = "test_by_check_edit"))