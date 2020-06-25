# -*- coding: utf-8 -*-
from modules.contact import Contact
import random
import time

def test_delete_contact(app, db, check_ui):
    if (len(db.get_contact_list()) == 0):
        app.contact.new_contact_creation(Contact(firstname="test_by_check_edit", middlename = "test_by_check_edit", lastname = "test_by_check_edit", nickname = "test_by_check_edit", title = "test_by_check_edit", company = "test_by_check_edit", address = "test_by_check_edit", home = "test_by_check_edit", mobile = "test_by_check_edit",
                                              work = "test_by_check_edit", fax ="test_by_check_edit", email = "test_by_check_edit", email1 = "test_by_check_edit", email2 = "test_by_check_edit", email3 = "test_by_check_edit", address2 = "test_by_check_edit", homepage = "test_by_check_edit", bday = "5", bmounth = "July",
                                              byear = "1982", aday = "2", amonth = "July", ayear = "2003", phone2 = "test_by_check_edit", notes = "test_by_check_edit"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    time.sleep(3)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if (check_ui):
        assert sorted(new_contacts, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max)




