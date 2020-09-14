#from modules.contact import Contact
import re
#from random import randrange
#def test_compare_contact_home_db(app, db):
#    contact_data_data_base = db.get_contact_list()
#    contact_data_home_page = app.contact.get_contact_list()
#    assert (sorted(contact_data_home_page, key=Contact.id_or_max)) == (sorted(contact_data_data_base, key=Contact.id_or_max))

#def test_a(app, db):
#    id_list, list_contact = db.get_contact_list()



def test_compare_home_edit_user_page(app,db):
    #list_contact, id_list  = db.get_contact_list()
    id_list = db.get_contact_id()

    #old_contacts = app.contact.count()
    #index = randrange(old_contacts)
    for i in id_list:
        contact_data_edit_page = app.contact.data_edit_page(i)
        print(contact_data_edit_page)
        #contact_data_home_page = db.get_contact_list()
        #print (contact_data_home_page)
        #assert clear(contact_data_edit_page.firstname) == contact_data_home_page.firstname
        #assert clear(contact_data_edit_page.lastname) == contact_data_home_page.lastname
        #assert merge_phones_like_on_homepage(contact_data_edit_page) == contact_data_home_page.all_phones
        #assert merge_emails_like_on_homepage(contact_data_edit_page) == contact_data_home_page.all_emails
        #assert clear(contact_data_edit_page.address) == contact_data_home_page.address


    #contact_data_edit_page = app.contact.data_edit_page(index+1)
    #contact_data_home_page = db.get_contact_list()[index]
    #assert clear(contact_data_edit_page.firstname) == contact_data_home_page.firstname
    #assert clear(contact_data_edit_page.lastname) == contact_data_home_page.lastname
    #assert merge_phones_like_on_homepage(contact_data_edit_page) == contact_data_home_page.all_phones
    #assert merge_emails_like_on_homepage(contact_data_edit_page) == contact_data_home_page.all_emails
    #assert clear(contact_data_edit_page.address) == contact_data_home_page.address

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.home, contact.mobile, contact.work, contact.phone2]))))

def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None, [contact.email, contact.email1, contact.email2]))))



#И так
#Я беру через базу данных все айдишники
#в контакте фикстуре получаю все данные относиетльно айдишника и нужно через урлу там
#и сравниваю чер цикл фор так как нужно прогнать все контакты
#'''