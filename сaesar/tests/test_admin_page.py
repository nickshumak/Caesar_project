from resource.users_base import *
from tests.test_base import TestBase
from caesar_items.pages.admin_page import *
from resource.url_site import PathUrl


class TestAdminPage(TestBase):
    def test_title_admin_page(self):
        """Checking title Admin page after transition from Group page"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        admin_page = AdminPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE) \
            .get_title_name()
        self.assertIn("Caesar Admin Panel", admin_page)

    def test_admin_escape_home_button(self):
        """Checking escape home button on admin page"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        admin_page = AdminPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE). \
            back_home() \
            .get_title_name()
        self.assertIn("Caesar", admin_page)

    def test_create_edit_users(self):
        """checking user after creating"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        admin_page = AdminPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE).tab_users() \
            .add_entity_user().fill_user_fields(
            'Donald', 'Tramp', "Teacher", "Dnipro", "123", "123", "123")
        expected_result = ["Donald"]
        actual_result = admin_page.get_table('users')
        self.assertIn(expected_result, actual_result)

    def test_create_edit_groups(self):
        """checking group after creating"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        admin_page = AdminPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE).tab_groups() \
            .add_entity_group().fill_group_fields(
            'DP-095JS', "Dnipro", False, 'MQC', "2018-05-15", "2018-07-15",
            "D. Petin", "M. Omel`chuk", "planned")
        actual_result = admin_page.get_table("groups")
        expected_result = ['DP-095JS']
        self.assertIn(expected_result, actual_result)

    def test_create_edit_students(self):
        """checking student after creating"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        admin_page = AdminPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE).tab_students() \
            .add_entity_student().fill_student_fields(
            "DP-095JS", "Victor", "Cesar", "Pre-intermediate",
            "", "", "100", "N. Varenko")
        actual_result = admin_page.get_table("students")
        expected_student = ['Victor']
        self.assertIn(expected_student, actual_result)

    def test_create_edit_void_fields_student(self):
        """checking student after creating"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        admin_page = AdminPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE).tab_students() \
            .add_entity_student().fill_student_fields(
            "", "", "", "",
            "", "", "", "")

        # actual_result = admin_page.get_table("students")
        # expected_student = ['']
        # self.assertIn(expected_student, actual_result)