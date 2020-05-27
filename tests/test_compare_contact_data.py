from modules.group import Group
import re
from random import randrange

def test_compare_home_edit_user_page(app):
    old_contacts = app.contact.count()
    index = randrange(old_contacts)
    contact_data_edit_page = app.contact.data_edit_page(index)
    contact_data_home_page = app.contact.get_contact_list()[index]
    assert clear(contact_data_edit_page.firstname) == contact_data_home_page.firstname
    assert clear(contact_data_edit_page.lastname) == contact_data_home_page.lastname
    assert merge_phones_like_on_homepage(contact_data_edit_page) == contact_data_home_page.all_phones
    assert merge_emails_like_on_homepage(contact_data_edit_page) == contact_data_home_page.all_emails
    assert clear(contact_data_edit_page.address) == contact_data_home_page.address

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email1, contact.email2]))))


