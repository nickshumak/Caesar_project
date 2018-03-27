import unittest
from resource.users_base import *
from tests.test_base import TestBase
from caesar_items.pages.admin_page import *
from caesar_items.locators import *
import time


class TestAdminPage(TestBase):
    def test_title_admin_page(self):
        """Checking title Admin page after transition from Group page"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        admin_page = AdminPage(self.driver). \
            get_page("http://localhost:3000/admin") \
            .get_title_name()
        time.sleep(2)
        self.assertIn("Caesar Admin Panel", admin_page)

    def test_admin_escape_home_button(self):
        """Checking escape home button on admin page"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        admin_page = AdminPage(self.driver). \
            get_page("http://localhost:3000/admin"). \
            back_home() \
            .get_title_name()
        self.assertIn("Caesar", admin_page)

    def test_create_edit_users(self):
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        admin_page = AdminPage(self.driver). \
            get_page("http://localhost:3000/admin").tab_users() \
            .add_entity_user().fill_user_fields(
            '123', "123", "Teacher", "Dnipro", "123", "123", "123")
        time.sleep(2)

    def test_create_edit_groups(self):
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        admin_page = AdminPage(self.driver). \
            get_page("http://localhost:3000/admin").tab_groups() \
            .add_entity_group().fill_group_fields(
            'DP-095JS', "Dnipro", False, 'MQC', "2018-05-15", "2018-07-15",
            "D. Petin", "M. Omel`chuk", "planned")
        time.sleep(2)

    def test_create_edit_students(self):
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        admin_page = AdminPage(self.driver). \
            get_page("http://localhost:3000/admin").tab_students() \
            .add_entity_student().fill_student_fields(
            "DP-095JS", "New", "Word", "Pre-intermediate", "http", "http", "100", "100")
        time.sleep(2)

