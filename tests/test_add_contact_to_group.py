from fixtures.orm import ORMFixture
from fixtures.db import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app):
    list_groups = db.get_group_list()
    list_id_groups = []
    for x in list_groups:
        list_id_groups.append(x.id)
    #print(list_id_groups)

    for y in list_id_groups:
        l = db.get_contacts_not_in_group(Group(id=y))
        #print (l)
        if len(l) > 0:
            app.contact.add_contact_to_group(int(l[0].id), y)
        #else:
        #    app.new_contact_creation()
        #    app.create_group()
        #    app.add_contact_to_group(l[0], y)



    #try:
    #    l = db.get_contacts_in_group(Group(id="284"))

     #   for item in l:
     #       print(item)
     #   print(len(l))
    #finally:
    #    pass #db.destroy()


#def test_add_contact_to_group()
