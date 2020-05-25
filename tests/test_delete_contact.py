# -*- coding: utf-8 -*-
from modules.contact import Contact
from random import randrange
import time

def test_delete_contact(app):
    if app.contact.count()==0:
        app.contact.new_contact_creation(Contact(firstname="test_by_check_edit", middlename = "test_by_check_edit", lastname = "test_by_check_edit", nickname = "test_by_check_edit", title = "test_by_check_edit", company = "test_by_check_edit", address = "test_by_check_edit", home = "test_by_check_edit", mobile = "test_by_check_edit",
                                              work = "test_by_check_edit", fax ="test_by_check_edit", email = "test_by_check_edit", email1 = "test_by_check_edit", email2 = "test_by_check_edit", email3 = "test_by_check_edit", address2 = "test_by_check_edit", homepage = "test_by_check_edit", bday = "5", bmounth = "July",
                                              byear = "1982", aday = "2", amonth = "July", ayear = "2003", phone2 = "test_by_check_edit", notes = "test_by_check_edit"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    time.sleep(3)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts [index:index+1] = []
    assert old_contacts == new_contacts




