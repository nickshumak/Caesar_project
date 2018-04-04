from resource.users_base import *
from tests.test_base import TestBase


class TestAdminPage(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)
        self.admin_page = self.group_page.open_admin_page()

    def test01_admin_escape_home_button(self):
        """ Checking escape home button on admin page."""
        self.admin_page.back_home()
        self.assertEqual("Caesar", self.admin_page.get_title_name())

    def test02_title_admin_page(self):
        """ Checking admin's title name."""
        title_page = self.admin_page.get_title_name()
        self.assertEqual("Caesar Admin Panel", title_page)

    def test03_create_edit_users(self):
        """ Checking user in user's table after creating."""
        actual_table = self.admin_page. \
            tab_users(). \
            add_entity_user(). \
            fill_user_name('User'). \
            fill_user_second_name('Tramp'). \
            fill_user_role_type('Teacher'). \
            fill_user_city('Dnipro'). \
            fill_user_photo('photo'). \
            fill_user_login('123'). \
            fill_user_password('123'). \
            submit(). \
            get_table('users')
        expected_result = ["User"]
        self.assertIn(expected_result, actual_table)

    def test04_create_edit_groups(self):
        """ Checking group after creating."""
        actual_table = self.admin_page. \
            tab_groups(). \
            add_entity_group(). \
            fill_group_name('DP-095JS'). \
            fill_group_geography('Dnipro'). \
            fill_group_owner(False). \
            fill_group_direct('MQC'). \
            fill_group_first_date('2018-05-15'). \
            fill_group_second_date('2018-07-15'). \
            fill_group_teacher_name('D. Petin'). \
            fill_group_experts_name('M. Omel`chuk'). \
            fill_group_stage_level('planned'). \
            submit()
        actual_result = actual_table.get_table("groups")
        expected_result = ['DP-095JS']
        self.assertIn(expected_result, actual_result)

    def test05_create_edit_students(self):
        """ Checking student after creating."""
        actual_table = self.admin_page. \
            tab_students(). \
            add_entity_student(). \
            fill_student_group_id('"DP-095JS'). \
            fill_student_name('Victor'). \
            fill_student_last_name('Cesar'). \
            fill_student_english_level('Pre-intermediate'). \
            fill_student_cv_url(''). \
            fill_student_entry_score('99'). \
            fill_student_approved_by('N. Varenko'). \
            submit(). \
            get_table('students')
        expected_student = ['Victor']
        self.assertIn(expected_student, actual_table)

    def test06_create_edit_empty_fields_student(self):
        """ Checking button after filling with empty fields.
        It will be failed."""
        is_enabled_submit_button = self.admin_page. \
            tab_students(). \
            add_entity_student(). \
            fill_student_group_id(''). \
            fill_student_name(''). \
            fill_student_last_name(''). \
            fill_student_english_level('Pre-intermediate'). \
            fill_student_cv_url(''). \
            fill_student_entry_score(''). \
            fill_student_approved_by(''). \
            is_enabled_submit_button
        self.assertFalse(is_enabled_submit_button)

    def test07_create_edit_empty_fields_group(self):
        """ Checking button after filling by empty fields.
        It will be failed."""
        is_enabled_submit_button = self.admin_page. \
            tab_groups(). \
            add_entity_group(). \
            fill_group_name(''). \
            fill_group_geography('Dnipro'). \
            fill_group_owner(False). \
            fill_group_direct('MQC'). \
            fill_group_first_date(''). \
            fill_group_second_date(''). \
            fill_group_teacher_name(''). \
            fill_group_experts_name(''). \
            fill_group_stage_level('planned'). \
            is_enabled_submit_button
        self.assertFalse(is_enabled_submit_button)

    def test08_create_edit_max_length_fields_user(self):
        """ Checking button after filling with more than max length.
        P.S max length of login/password field is 10 symbols.
        It will be failed."""
        is_enabled_submit_button = self.admin_page. \
            tab_users(). \
            add_entity_user(). \
            fill_user_name('Coder'). \
            fill_user_second_name('Developerovich'). \
            fill_user_role_type('Teacher'). \
            fill_user_city('Dnipro'). \
            fill_user_photo('photo'). \
            fill_user_login('b' * 11). \
            fill_user_password('a' * 11). \
            is_enabled_submit_button()
        self.assertFalse(is_enabled_submit_button)

    def test09_create_edit_symbols_user(self):
        """ Checking button after filling with symbols
        It will be failed."""
        is_enabled_submit_button = self.admin_page. \
            tab_users(). \
            add_entity_user(). \
            fill_user_name('Coder'). \
            fill_user_second_name('Developerovich'). \
            fill_user_role_type('Teacher'). \
            fill_user_city('Dnipro'). \
            fill_user_photo('photo'). \
            fill_user_login('b' * 11). \
            fill_user_password('a' * 11). \
            is_enabled_submit_button()
        self.assertFalse(is_enabled_submit_button)

    def test10_delete_user_after_create(self):
        """ Checking users' table after deleting
        user who has been added recently."""
        actual_table = self.admin_page. \
            tab_users(). \
            add_entity_user(). \
            fill_user_name('Sergei'). \
            fill_user_second_name('D'). \
            fill_user_role_type('Teacher'). \
            fill_user_city('Dnipro'). \
            fill_user_photo('photo'). \
            fill_user_login('Vlad'). \
            fill_user_password('1234'). \
            submit(). \
            delete_last_entity(). \
            get_table('users')
        self.assertNotIn('Sergei', actual_table)
