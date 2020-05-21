# -*- coding: utf-8 -*-
from modules.contact import Contact

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.new_contact_creation(
            Contact(firstname="Test_Firstname", middlename="Test_Middlename", lastname="Test_lastname",
                    nickname="Test_Nickname", title="Test_title", company="Company", address="Test_adress", home="Home",
                    mobile="mobile",
                    work="Test_work", fax="Test_fax", email="Test_email", email1="Test_email1", email2="Test_email2",
                    email3="Test_email3", address2="Test_adress2", homepage="Test_homepage", bday="5", bmounth="July",
                    byear="1982", aday="2", amonth="July", ayear="2003", phone2="Test_phone2", notes="Test_notes"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_contact(Contact(firstname="test_by_check_edit", middlename = "test_by_check_edit", lastname = "test_by_check_edit", nickname = "test_by_check_edit", title = "test_by_check_edit", company = "test_by_check_edit", address = "test_by_check_edit", home = "test_by_check_edit", mobile = "test_by_check_edit",
                                              work = "test_by_check_edit", fax ="test_by_check_edit", email = "test_by_check_edit", email1 = "test_by_check_edit", email2 = "test_by_check_edit", email3 = "test_by_check_edit", address2 = "test_by_check_edit", homepage = "test_by_check_edit", bday = "5", bmounth = "July",
                                              byear = "1982", aday = "2", amonth = "July", ayear = "2003", phone2 = "test_by_check_edit", notes = "test_by_check_edit"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_edit_contact_few_fields(app):
    if app.contact.count() ==0:
        app.contact.new_contact_creation(Contact(firstname="test_by_check_edit", middlename = "test_by_check_edit", lastname = "test_by_check_edit", nickname = "test_by_check_edit", title = "test_by_check_edit", company = "test_by_check_edit", address = "test_by_check_edit", home = "test_by_check_edit", mobile = "test_by_check_edit",
                                              work = "test_by_check_edit", fax ="test_by_check_edit", email = "test_by_check_edit", email1 = "test_by_check_edit", email2 = "test_by_check_edit", email3 = "test_by_check_edit", address2 = "test_by_check_edit", homepage = "test_by_check_edit", bday = "5", bmounth = "July",
                                              byear = "1982", aday = "2", amonth = "July", ayear = "2003", phone2 = "test_by_check_edit", notes = "test_by_check_edit"))
    app.contact.edit_contact(Contact(middlename="MIDDLENAME!!!!!!!!!!!!!", lastname="LASTNAME!!!!!!!!!!!", nickname="NICKNAME!!!!!!!!!!!!!"))




