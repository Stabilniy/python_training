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
    assert clear(contact_data_edit_page.home) == contact_data_home_page.home
    assert clear(contact_data_edit_page.mobile) == contact_data_home_page.mobile
    assert clear(contact_data_edit_page.work) == contact_data_home_page.work
    assert clear(contact_data_edit_page.phone2) == contact_data_home_page.phone2
    assert clear(contact_data_edit_page.address) == contact_data_home_page.address
    assert clear(contact_data_edit_page.email) == contact_data_home_page.email
    assert clear(contact_data_edit_page.email1) == contact_data_home_page.email1
    assert clear(contact_data_edit_page.email2) == contact_data_home_page.email2

def clear(s):
    return re.sub("[() -]","", s)

'''
def test_compare_profile_view_edit_user_page(app):
    contact_data_edit_page = app.contact.data_edit_page(0)
    contact_data_view_page = app.contact.data_view_page(0)
    assert contact_data_edit_page.firstname == contact_data_view_page.firstname
    assert contact_data_edit_page.lastname == contact_data_view_page.lastname
    assert contact_data_edit_page.home == contact_data_view_page.home
    assert contact_data_edit_page.mobile == contact_data_view_page.mobile
    assert contact_data_edit_page.work == contact_data_view_page.work

'''
