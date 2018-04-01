from resource.users_base import *
from tests.test_base import TestBase
from resource.url_site import PathUrl


class TestAdminPage(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)
        self.admin_page = self.group_page.open_admin_page()

    def test_admin_escape_home_button(self):
        """Checking escape home button on admin page"""
        self.admin_page.back_home()
        self.assertEqual("Caesar", self.admin_page.get_title_name())

    def test_title_admin_page(self):
        title_page = self.admin_page.get_title_name()
        self.assertEqual("Caesar Admin Panel", title_page)

    def test_create_edit_users(self):
        """checking user in user's table after creating"""
        actual_table = self.admin_page. \
            tab_users(). \
            add_entity_user(). \
            fill_user_name('User'). \
            fill_user_second_name('Tramp'). \
            fill_user_type_role('Teacher'). \
            fill_user_city('Dnipro'). \
            fill_user_photo('photo'). \
            fill_user_login('123'). \
            fill_user_password('123'). \
            submit(). \
            get_table('users')
        expected_result = ["User"]
        self.assertIn(expected_result, actual_table)

    def test_create_edit_groups(self):
        """checking group after creating"""
        actual_table = self.admin_page. \
            tab_groups(). \
            add_entity_group(). \
            fill_group_name('DP-095JS'). \
            fill_group_geography('Dnipro'). \
            fill_group_owner(False). \
            fill_group_direct('MQC'). \
            fill_group_first_date('2018-05-15'). \
            fill_group_second_date('2018-07-15'). \
            fill_group_name_teacher('D. Petin'). \
            fill_group_name_experts('M. Omel`chuk'). \
            fill_group_level_stage('planned'). \
            submit()
        actual_result = actual_table.get_table("groups")
        expected_result = ['DP-095JS']
        self.assertIn(expected_result, actual_result)

    def test_create_edit_students(self):
        """checking student after creating"""
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

    def test_create_edit_empty_fields_student(self):
        """checking student after creating with empty fields
        It will be failed"""
        actual_condition_button = self.admin_page. \
            tab_students(). \
            add_entity_student(). \
            fill_student_group_id(''). \
            fill_student_name(''). \
            fill_student_last_name(''). \
            fill_student_english_level('Pre-intermediate'). \
            fill_student_cv_url(''). \
            fill_student_entry_score(''). \
            fill_student_approved_by(''). \
            get_condition_button()
        self.assertFalse(actual_condition_button)

    def test_create_edit_empty_fields_group(self):
        """checking group after creating group with empty fields
        It will be failed"""
        actual_condition_button = self.admin_page. \
            tab_groups(). \
            add_entity_group(). \
            fill_group_name(''). \
            fill_group_geography('Dnipro'). \
            fill_group_owner(False). \
            fill_group_direct('MQC'). \
            fill_group_first_date(''). \
            fill_group_second_date(''). \
            fill_group_name_teacher(''). \
            fill_group_name_experts(''). \
            fill_group_level_stage('planned'). \
            get_condition_button()
        self.assertFalse(actual_condition_button)

    def test_create_edit_max_length_fields_user(self):
        """checking user after creating with more than max length
        P.S max length of login/password field is 10 symbols
        It will be failed"""
        actual_condition_button = self.admin_page. \
            get_page(PathUrl.ADMIN_PAGE).tab_users(). \
            add_entity_user(). \
            fill_user_name('Coder'). \
            fill_user_second_name('Developerovich'). \
            fill_user_type_role('Teacher'). \
            fill_user_city('Dnipro'). \
            fill_user_photo('photo'). \
            fill_user_login('b' * 11). \
            fill_user_password('a' * 11). \
            get_condition_button()
        self.assertFalse(actual_condition_button)
