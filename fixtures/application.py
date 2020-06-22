from selenium import webdriver
from fixtures.session import SessionHelper
from fixtures.contact import ContactHelper
from fixtures.group import GroupHelper
#from fixtures.db import DbFixture

class Application:

    def __init__(self, browser, base_url):
        if browser == "ie":
            self.wd = webdriver.Ie()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)
        self.group = GroupHelper(self)
        #self.db = DbFixture(self)
        self.base_url = base_url

    def open_homepage(self):
        wd = self.wd
        if wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_xpath("//form[@name='MainForm']//div[1]//input[1]")) > 0:
            return
        wd.get(self.base_url)
        
        
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


    