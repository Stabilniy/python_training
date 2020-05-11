class GroupHelper:

    def __init__(self, app):
        self.app = app
    
    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()
        
        
    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
    
    
    def create_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_xpath("//div[@id='content']/div").click()
        self.return_to_group_page()

    def edit(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_xpath("//span[1]//input[1]").click()
        wd.find_element_by_name("edit").click()
        self.fill_group_form(group)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def delete(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_xpath("//span[1]//input[1]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()








    
    
    