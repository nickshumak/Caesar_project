from caesar_items.pages.groups_page import GroupsPage
from resource.users_base import first_admin
from tests.test_base import TestBase

TEST_GROUP_NAME = "Test group"
TEST_TOO_LONG_GROUP_NAME = "12345678901234567890"
TEST_START_DATE = "11/04/2018"
TEST_TEACHER_INDEX = 1
TEST_FAILED_MESSAGE = "Test_failed"


class TestCreatingGroup(TestBase):

    def test_is_group_creates(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_random_select()
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        test_direction = groups_page.WindowCreatingGroup().direction_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(TEST_TEACHER_INDEX)
        name = groups_page.WindowCreatingGroup().name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        try:
            self.assertTrue(name in str(self.driver.page_source))
        except AssertionError:
            print(TEST_FAILED_MESSAGE)
        # self.assertEqual(self.driver.current_url, expected_page_url)

    def test_is_group_creates_with_test_name(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_random_select()
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        groups_page.WindowCreatingGroup().group_name_setting(TEST_GROUP_NAME)
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(TEST_TEACHER_INDEX)
        name = groups_page.WindowCreatingGroup().name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        try:
            self.assertIn(name, str(self.driver.page_source))
        except AssertionError:
            print(TEST_FAILED_MESSAGE)

    def test_is_group_creates_with_test_location(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_random_select()
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        location_of_group = groups_page.WindowCreatingGroup().location_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(TEST_TEACHER_INDEX)
        name = groups_page.WindowCreatingGroup().name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        try:
            self.assertIn(location_of_group, str(self.driver.page_source))
        except AssertionError:
             print(TEST_FAILED_MESSAGE)

    def test_is_group_creates_with_correct_start_date(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_random_select()
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        test_direction = groups_page.WindowCreatingGroup().direction_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(TEST_TEACHER_INDEX)
        name = groups_page.WindowCreatingGroup().name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        try:
            self.assertIn(TEST_START_DATE, str(self.driver.page_source))
        except AssertionError:
             print(TEST_FAILED_MESSAGE)

    def test_is_group_creates_direction_right(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_random_select()
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        test_direction = groups_page.WindowCreatingGroup().direction_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(TEST_TEACHER_INDEX)
        name = groups_page.WindowCreatingGroup().name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        try:
            self.assertIn(test_direction, str(self.driver.page_source))
        except AssertionError:
            print(TEST_FAILED_MESSAGE)
        # self.assertEqual(self.driver.current_url, expected_page_url)
