from modules.contact import Contact

def test_compare_contact_home_db(app, db):
    contact_data_data_base = db.get_contact_list()
    contact_data_home_page = app.contact.get_contact_list()
    assert (sorted(contact_data_home_page, key=Contact.id_or_max)) == (sorted(contact_data_data_base, key=Contact.id_or_max))




