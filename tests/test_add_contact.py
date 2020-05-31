# -*- coding: utf-8 -*-
from modules.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + '_'.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#test_data = [Group(name="testname", header="testheader", footer="testfooter")] + [
#             Group(name = random_string("name", 10), header= random_string("header", 20), footer = random_string("footer", 15)) for i in range(10)]


test_data = [Contact(firstname= random_string("firstname", 15 ), middlename = random_string("middlename", 10), lastname = random_string("lastname", 20) , nickname = random_string("nickname", 13) , title = random_string("title", 12) , company = random_string("company", 11) , address = random_string("address", 14) , home = random_string("home", 21), mobile = random_string("mobile", 10),
                                              work = random_string("work", 11), fax = random_string("fax", 10), email = random_string("email", 18) , email1 = random_string("email1", 12), email2 = random_string("email2", 21) , email3 = random_string("email3", 10), address2 = random_string("address2", 17) , homepage = random_string("homepage", 14), phone2 = random_string("phone2", 10), notes = random_string("notes", 14)) for i in range(3)]


@pytest.mark.parametrize("contact", test_data, ids=[repr(x) for x in test_data])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.new_contact_creation(contact)
    assert len(old_contacts) +1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

