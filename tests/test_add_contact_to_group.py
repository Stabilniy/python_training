from fixtures.orm import ORMFixture
from modules.contact import Contact
from modules.group import Group
from fixtures.db import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
def test_add_contact_to_group(app):
    if (len(db.get_contact_list()) == 0):
        app.contact.new_contact_creation(
            Contact(firstname="Test_Firstname", middlename="Test_Middlename", lastname="Test_lastname",
                    nickname="Test_Nickname", title="Test_title", company="Company", address="Test_adress", home="Home",
                    mobile="mobile",
                    work="Test_work", fax="Test_fax", email="Test_email", email1="Test_email1", email2="Test_email2",
                    email3="Test_email3", address2="Test_adress2", homepage="Test_homepage", bday="5", bmounth="July",
                    byear="1982", aday="2", amonth="July", ayear="2003", phone2="Test_phone2", notes="Test_notes"))
    if app.group.count() == 0:
        app.group.create_group(Group(name="username", header="testheader", footer="testfooter"))
    if db.get_not_related_group_contact() == False:
        app.contact.new_contact_creation(
            Contact(firstname="Test_Firstname", middlename="Test_Middlename", lastname="Test_lastname",
                    nickname="Test_Nickname", title="Test_title", company="Company", address="Test_adress", home="Home",
                    mobile="mobile",
                    work="Test_work", fax="Test_fax", email="Test_email", email1="Test_email1", email2="Test_email2",
                    email3="Test_email3", address2="Test_adress2", homepage="Test_homepage", bday="5", bmounth="July",
                    byear="1982", aday="2", amonth="July", ayear="2003", phone2="Test_phone2", notes="Test_notes"))

    free_contact, free_group = db.get_not_related_group_contact()
    app.contact.add_contact_to_group(free_contact, str(free_group))
    assert str(free_contact) in db.get_list_id_contact_in_group(Group(id=free_group))
    app.contact.delete_contact_from_group(free_contact, free_group)
    assert str(free_contact) not in db.get_list_id_contact_in_group(Group(id=free_group))
