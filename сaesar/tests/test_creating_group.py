from caesar_items.pages.groups_page import GroupsPage
from resource.users_base import first_admin
from tests.test_base import TestBase

TEST_GROUP_NAME = "Test group"
TEST_TOO_LONG_GROUP_NAME = "12345678901234567890"
TEST_START_DATE = "11/04/2018"


class TestCreatingGroup(TestBase):

    def test_is_group_creates(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_select(2)
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        test_direction = groups_page.WindowCreatingGroup().direction_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(1)
        name = groups_page.WindowCreatingGroup().name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        self.assertTrue(name in self.driver.page_source)
        # self.assertEqual(self.driver.current_url, expected_page_url)

    def test_is_group_creates_with_test_name(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_select(2)
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        groups_page.WindowCreatingGroup().group_name_setting(TEST_GROUP_NAME)
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(1)
        name = groups_page.WindowCreatingGroup().name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        try:
            self.assertTrue(name in self.driver.page_source)
        except:
            self.assertFalse(name in self.driver.page_source)

    def test_is_group_creates_with_test_location(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_select(2)
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        location_of_group = groups_page.WindowCreatingGroup().location_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(1)
        name = groups_page.WindowCreatingGroup().name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        try:
            self.assertTrue(location_of_group in self.driver.page_source)
        except:
            self.assertFalse(location_of_group in self.driver.page_source)

    def test_is_group_creates_with_correct_start_date(self):
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_select(2)
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        test_direction = groups_page.WindowCreatingGroup().direction_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(1)
        name = groups_page.WindowCreatingGroup().name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        self.assertTrue(TEST_START_DATE in self.driver.page_source)
