# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from group import Group

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_add_group(self):
        wd = self.wd
        self.login(username = "admin", password = "secret")
        self.create_group(Group(name = "testname", header = "testheader", footer = "testfooter"))
        self.logout()


    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()


    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()


    def create_group(self, group):
        wd = self.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_xpath("//div[@id='content']/div").click()
        self.return_to_group_page()


    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()


    def login(self, username, password):
        wd = self.wd
        self.open_homepage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()


    def open_homepage(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        return wd

    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()

