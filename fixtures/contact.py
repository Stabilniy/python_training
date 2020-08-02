from selenium.webdriver.support.ui import Select
import time
from modules.contact import Contact
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def new_contact_creation(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_homepage()
        self.contact_cache = None

    def select_contacts_by_index(self,index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contacts_by_id(self, id):
        wd = self.app.wd
        #wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath("//input[@id='%s']" % id).click()

    def delete(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        time.sleep(5)
        self.select_contacts_by_index(index)
        wd.find_element_by_xpath("//div[2]//input[1]").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_homepage()
        time.sleep(5)
        self.select_contacts_by_id(id)
        wd.find_element_by_xpath("//div[2]//input[1]").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None


    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_selectlist_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def edit_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, contact, index):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.app.open_homepage()
        wd.get("http://localhost/addressbook/edit.php?id='%s'" %id)
        #wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_filed_value("firstname", contact.firstname)
        self.change_filed_value("middlename", contact.middlename)
        self.change_filed_value("lastname", contact.lastname)
        self.change_filed_value("nickname", contact.nickname)
        self.change_filed_value("title", contact.title)
        self.change_filed_value("company", contact.company)
        self.change_filed_value("address", contact.address)
        self.change_filed_value("home", contact.home)
        self.change_filed_value("mobile", contact.mobile)
        self.change_filed_value("work", contact.work)
        self.change_filed_value("fax", contact.fax)
        self.change_filed_value("email", contact.email)
        self.change_filed_value("email2", contact.email2)
        self.change_filed_value("email3", contact.email3)
        self.change_filed_value("address2", contact.address2)
        self.change_filed_value("homepage", contact.homepage)
        self.change_selectlist_value("bday", contact.bday)
        self.change_selectlist_value("bmonth", contact.bmounth)
        self.change_filed_value("byear", contact.byear)
        self.change_selectlist_value("aday", contact.aday)
        self.change_selectlist_value("amonth", contact.amonth)
        self.change_filed_value("ayear", contact.ayear)
        self.change_filed_value("phone2", contact.phone2)
        self.change_filed_value("notes", contact.notes)

    def count(self):
        wd = self.app.wd
        self.app.open_homepage()
        return len(wd.find_elements_by_name("selected[]"))
    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_homepage()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(firstname=firstname, lastname = lastname, id=id, address = address , all_phones = all_phones, all_emails = all_emails))
        return list(self.contact_cache)

    #def get_contact_list(self):
    #    if self.contact_cache is None:
    #        wd = self.app.wd
    #        self.app.open_homepage()
    #        self.contact_cache = []
    #        for row in wd.find_elements_by_name("entry"):
    #            cells = row.find_elements_by_tag_name("td")
    #            id = cells[0].find_element_by_tag_name("input").get_attribute("value")
    #            firstname = cells[2].text
    #            lastname = cells[1].text
    #            address = cells[3].text
    #            all_emails = cells[4].text
    #            all_phones = cells[5].text
    #            self.contact_cache.append(Contact(firstname=firstname, lastname = lastname, id=id, all_emails = all_emails))
    #   return list(self.contact_cache)


    def get_edit_page(self, index):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def data_edit_page(self, index):
        wd = self.app.wd
        self.get_edit_page(index)
        firstname = wd.find_element_by_xpath("//input[@name='firstname']").get_attribute("value")
        lastname = wd.find_element_by_xpath("//input[@name='lastname']").get_attribute("value")
        address = wd.find_element_by_xpath("//textarea[@name='address']").get_attribute("value")
        home = wd.find_element_by_xpath("//input[@name='home']").get_attribute("value")
        mobile = wd.find_element_by_xpath("//input[@name='mobile']").get_attribute("value")
        work = wd.find_element_by_xpath("//input[@name='work']").get_attribute("value")
        phone2 = wd.find_element_by_xpath("//input[@name='phone2']").get_attribute("value")
        email = wd.find_element_by_xpath("//input[@name='email']").get_attribute("value")
        email1 = wd.find_element_by_xpath("//input[@name='email2']").get_attribute("value")
        email2 = wd.find_element_by_xpath("//input[@name='email3']").get_attribute("value")
        return Contact(firstname = firstname, lastname = lastname , address = address, home = home, mobile = mobile, work = work, phone2 = phone2, email = email, email1 = email1, email2 = email2)

    def add_contact_to_group(self, id_contact, id_group):
        wd = self.app.wd
        self.select_contacts_by_id(id_contact)
        Select(wd.find_element_by_name("to_group")).select_by_value(id_group)
        wd.find_element_by_name("add").click()

    def delete_contact_from_group(self, id_contact, id_group):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/?group='%s'" %id_group)
        self.select_contacts_by_id(id_contact)
        wd.find_element_by_name("remove").click()








