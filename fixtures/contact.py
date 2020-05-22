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


    def delete(self):
        wd = self.app.wd
        self.app.open_homepage()
        time.sleep(5)
        wd.find_element_by_name("selected[]").click()
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
            #wd.find_element_by_name(field_name).click()

    def edit_contact(self, contact):
        wd = self.app.wd
        self.app.open_homepage()
        wd.find_element_by_xpath("//tr[2]//td[8]//a[1]//img[1]").click()
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
            for element in wd.find_elements_by_name("entry"):
                i = element.find_element_by_xpath(".//td[1]")
                id = i.find_element_by_name("selected[]").get_attribute("value")
                text = element.find_element_by_xpath(".//td[3]").text
                self.contact_cache.append(Contact(firstname=text, id=id))
        return list(self.contact_cache)




