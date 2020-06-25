from modules.group import Group

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_name("submit").click()
        wd.find_element_by_xpath("//div[@id='content']/div").click()
        self.return_to_group_page()
        self.cache_group = None

    def edit(self, new_group):
        wd = self.app.wd
        self.edit_group_by_index(new_group, 0)

    def edit_group_by_index(self, new_group, index):
        wd = self.app.wd
        self.open_groups_page()
        #wd.find_elements_by_name("selected")[index].click()
        self.select_group_by_index(index)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.cache_group = None

    def edit_group_by_id(self, new_group, id):
        wd = self.app.wd
        self.open_groups_page()
        #wd.find_elements_by_name("selected")[index].click()
        self.select_group_by_id(id)
        wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()
        self.cache_group = None

    def change_filed_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        self.change_filed_value("group_name", group.name)
        self.change_filed_value("group_header", group.header)
        self.change_filed_value("group_footer", group.footer)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        #wd.find_element_by_xpath("//body//span['%s']" % id).click()
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def delete(self):
        wd = self.app.wd
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.cache_group = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(id)
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()
        self.cache_group = None


    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))
    cache_group = None

    def get_group_list(self):
        if self.cache_group is None:
            wd = self.app.wd
            self.open_groups_page()
            self.cache_group = []
            for element in wd.find_elements_by_xpath("//body//span"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.cache_group.append(Group(name = text, id = id))
        return list(self.cache_group)















    
    
    