from selenium import webdriver
from fixtures.session import SessionHelper
from fixtures.contact import ContactHelper
from fixtures.group import GroupHelper

class Application:


    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
 
 
    def open_homepage(self):
        wd = self.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//form[@name='MainForm']//div[1]//input[1]")) > 0:
            return
        wd.get("http://localhost/addressbook/")
        
        
    def return_to_homepage(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def destroy(self):
        self.wd.quit()


    