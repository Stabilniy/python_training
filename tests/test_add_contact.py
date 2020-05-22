# -*- coding: utf-8 -*-
from modules.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Test_Firstname01", middlename = "Test_Middlename", lastname = "Test_lastname", nickname = "Test_Nickname", title = "Test_title", company = "Company", address = "Test_adress", home = "Home", mobile = "mobile",
                                              work = "Test_work", fax ="Test_fax", email = "Test_email", email1 = "Test_email1", email2 = "Test_email2", email3 = "Test_email3", address2 = "Test_adress2", homepage = "Test_homepage", bday = "5", bmounth = "July",
                                              byear = "1982", aday = "2", amonth = "July", ayear = "2003", phone2 = "Test_phone2", notes = "Test_notes")
    app.contact.new_contact_creation(contact)

    #old_contacts.append(contact)
    assert len(old_contacts) +1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

