from caesar_items.pages.groups_page import GroupsPage
from resource.users_base import first_admin, coordinator
from tests.test_base import TestBase

TEST_GROUP_NAME = "Test group"
TEST_TOO_LONG_GROUP_NAME = "12345678901234567890"
TEST_START_DATE = "11/04/2018"
TEST_TEACHER_INDEX = 1
TEST_FAILED_MESSAGE = "Test_failed"


class TestCreatingGroup(TestBase):

    def test_is_group_creates(self):
        """
                Used role is Admin

                Test  can the group can be created at all
                :return:

                  """
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_random_select()
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        test_direction = groups_page.WindowCreatingGroup(). \
            direction_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(TEST_TEACHER_INDEX)
        name = groups_page.WindowCreatingGroup(). \
            name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        self.assertTrue(name in str(self.driver.page_source))

    def test_is_group_creates_with_test_name(self):
        """
          Used role is Admin
        Test can group be created with manual entering of it's name
        :return:

        """
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_random_select()
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        groups_page.WindowCreatingGroup().field_group_name_setting(TEST_GROUP_NAME)
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(TEST_TEACHER_INDEX)
        name = groups_page.WindowCreatingGroup(). \
            name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        self.assertIn(name, str(self.driver.page_source))

    def test_is_group_creates_with_test_location(self):
        """
          Used role is Admin
        Test  does location is saved when group is created

        :return:
        """
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_random_select()
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        location_of_group = groups_page.WindowCreatingGroup(). \
            location_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(TEST_TEACHER_INDEX)
        name = groups_page.WindowCreatingGroup(). \
            name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        self.assertIn(location_of_group, str(self.driver.page_source))

    def test_is_group_creates_with_correct_start_date(self):
        """
          Used role is Admin
                Test  does start date is saved when group is created

                :return:
                """
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_random_select()
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        test_direction = groups_page.WindowCreatingGroup(). \
            direction_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(TEST_TEACHER_INDEX)
        name = groups_page.WindowCreatingGroup().name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        self.assertIn(TEST_START_DATE, str(self.driver.page_source))

    def test_is_group_creates_direction_right(self):
        """
                        Test  does direction is saved when group is created

                        :return:
                        """
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        groups_page.WindowCreatingGroup().direction_of_group_random_select()
        groups_page.WindowCreatingGroup().location_of_group_random_select()
        test_direction = groups_page.WindowCreatingGroup(). \
            direction_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().date_start_setting(TEST_START_DATE)
        groups_page.WindowCreatingGroup().teachers_adding(TEST_TEACHER_INDEX)
        name = groups_page.WindowCreatingGroup().name_of_group_save_to_variable()
        groups_page.WindowCreatingGroup().submit_group_creating()
        self.assertIn(test_direction, str(self.driver.page_source))

    def test_name_entering_is_enabled(self):
        """
                Used role is Admin

                Test  is the field 'name' enabled
                :return:

                  """
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        field_name_of_group = groups_page.WindowCreatingGroup(). \
            field_group_name_appeal_to()
        self.assertTrue(field_name_of_group.is_enabled())

    def test_select_direction_is_enabled(self):
        """
                Used role is Admin

                Test  is the field 'direction' enabled
                :return:

                  """
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        field_direction = groups_page.WindowCreatingGroup(). \
            direction_of_group_appeal_to()
        self.assertTrue(field_direction.is_enabled())

    def test_select_location_is_enabled_for_admin(self):
        """
                Used role is Admin

                Test  is the field 'location' enabled
                :return:

                  """
        first_admin.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        field_location = groups_page.WindowCreatingGroup(). \
            location_of_group_appeal_to()
        self.assertTrue(field_location.is_enabled())

    def test_select_direction_is_enabled_for_coordinator(self):
        """
                Used role is Coordinator

                Test  is the field 'direction' enabled
                :return:

                  """
        coordinator.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        field_direction = groups_page.WindowCreatingGroup(). \
            direction_of_group_appeal_to()
        self.assertTrue(field_direction.is_enabled())

    def test_select_location_is_enabled_for_coordinator(self):
        """
                Used role is Coordinator

                Test  is the field 'location' enabled
                :return:

                  """
        coordinator.auto_login_n_open_group_page(self.login_page)
        groups_page = GroupsPage(self.driver)
        left_menu = groups_page.left_menu_open()
        button_create_group = left_menu.create_group()
        button_create_group.click()
        field_location = groups_page.WindowCreatingGroup(). \
            location_of_group_appeal_to()
        self.assertFalse(field_location.is_enabled())
