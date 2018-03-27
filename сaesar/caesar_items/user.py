import time
from caesar_items.pages.groups_page import GroupsPage


class User(object):
    def __init__(self, first_name, last_name, role, location, login, password) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.location = location
        self.login = login
        self.password = password
        self.full_name = first_name + '\n' + last_name

    def auto_login_n_open_group_page(self, login_page):
        """

        This function auto login user and open Group page
        :param login_page:
        """
        login_page.enter_login(self.login)
        login_page.enter_password(self.password)
        login_page.submit()
        time.sleep(1)




