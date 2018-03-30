from resource.users_base import *
from tests.test_base import TestBase
from caesar_items.pages.admin_page import *
from resource.url_site import PathUrl


class TestAdminPage(TestBase):

    def test_admin_escape_home_button(self):
        """Checking escape home button on admin page"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        title_page = GroupsPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE). \
            back_home(). \
            get_title_name()
        self.assertEqual("Caesar", title_page)

    def test_title_admin_page(self):
        """Checking title Admin page after transition from Group page"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        title_page = GroupsPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE). \
            get_title_name()
        self.assertEqual("Caesar Admin Panel", title_page)

    def test_create_edit_users(self):
        """checking user in user's table after creating"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        actual_table = GroupsPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE). \
            tab_users(). \
            add_entity_user(). \
            fill_user_name('Donald'). \
            fill_user_second_name('Tramp'). \
            fill_user_type_role('Teacher'). \
            fill_user_city('Dnipro'). \
            fill_user_photo('photo'). \
            fill_user_login('123'). \
            fill_user_password('123'). \
            submit(). \
            get_table('users')
        expected_result = ["Donald"]
        self.assertIn(expected_result, actual_table)

    def test_create_edit_groups(self):
        """checking group after creating"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        actual_table = GroupsPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE). \
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
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        actual_table = GroupsPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE).tab_students() \
            .add_entity_student(). \
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
        """checking student after creating with empty fields"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        actual_condition_button = GroupsPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE).tab_groups(). \
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
        """checking group after creating group with empty fields"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        actual_condition_button = GroupsPage(self.driver). \
            get_page(PathUrl.ADMIN_PAGE).tab_groups() \
            .add_entity_group(). \
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
        P.S max length of login/password field is 10 symbols"""
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        actual_condition_button = GroupsPage(self.driver). \
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
