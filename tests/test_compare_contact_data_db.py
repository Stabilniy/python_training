#from modules.group import Group
#import re
#from random import randrange

#from fixtures.orm import ORMFixture
from modules.contact import Contact
#from fixtures.db import Group

#db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


#try:
#    l = db.get_contact_list()
#    for item in l:
#        print(item)
#    print(len(l))
#finally:
#    pass #db.destroy()



def test_compare_contact_home_db(app, db):
    #old_contacts = app.contact.count()
    #index = randrange(old_contacts)
    #contact_data_edit_page = app.contact.data_edit_page(index)
    contact_data_home_page = app.contact.get_contact_list()
    #contact_data_data_base = merge_emails_like_on_homepage(db.get_contact_list())
    contact_data_base = db.get_contact_list()
    print(contact_data_home_page[0].all_emails)
    print(contact_data_home_page)
#    print(contact_data_base)
    #assert (sorted(contact_data_home_page, key=Contact.id_or_max)) == (sorted(contact_data_data_base, key=Contact.id_or_max))

#def clear(s):
    #return re.sub("[() -]", "", s)

#def merge_emails_like_on_homepage(contact):

#    return "\n".join(contact.email, contact.email1, contact.email2)


#def merge_emails_like_on_homepage(contact):
#    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email1, contact.email2]))))



    #print(contact_data_data_base)
    #print(sorted(contact_data_home_page, key=Contact.id_or_max))



'''
    assert clear(contact_data_edit_page.firstname) == contact_data_home_page.firstname
    assert clear(contact_data_edit_page.lastname) == contact_data_home_page.lastname
    assert merge_phones_like_on_homepage(contact_data_edit_page) == contact_data_home_page.all_phones
    assert merge_emails_like_on_homepage(contact_data_edit_page) == contact_data_home_page.all_emails
    assert clear(contact_data_edit_page.address) == contact_data_home_page.address

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2]))))

'''