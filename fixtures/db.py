import pymysql.cursors
from modules.group import Group
from modules.contact import Contact

class DbFixture():
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list


    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, company, firstname, lastname, email, email2, email3, home, mobile, work, phone2, address from addressbook")
            for row in cursor:
                (id, company, firstname, lastname, email, email2, email3, home, mobile, work, phone2, address) = row
                all_emails = "\n".join([email, email2, email3])
                all_phones = "\n".join([home, mobile, work, phone2])

                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname, all_emails=all_emails, all_phones=all_phones, address = address))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()