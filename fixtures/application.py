from selenium import webdriver
#from selenium.webdriver.support.ui import Select
from fixtures.session import SessionHelper
from fixtures.contact import ContactHelper
from fixtures.group import GroupHelper

class Application:


    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
 
 
    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        
        
    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()


    def destroy(self):
        self.wd.quit()


    