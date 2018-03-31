from caesar_items.pages.groups_page import GroupsPage
from resource.users_base import first_admin, coordinator
from tests.test_base import TestBase

TEST_GROUP_NAME = "Test group"
TEST_TOO_LONG_GROUP_NAME = "12345678901234567890123123123123123123123123123"
TEST_START_DATE = "11/04/2018"
TEST_TEACHER_INDEX = 1
TEST_FAILED_MESSAGE = "Test_failed"
MESSAGE_NAME_IS_MORE_20_CHAR = 'Name must be at most 20 characters!'
MESSAGE_DIRECTION_IS_NOT_SELECTED = 'Please, select direction!'
MESSAGE_START_DATE_FIELD_IS_EMPTY = 'Start date is required!'
MESSAGE_FINISH_DATE_FIELD_IS_EMPTY = 'Finish date is required!'


class TestCreatingGroup(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)
        self.left_menu = self.group_page.open_left_menu()
        self.left_menu.create_group().click()

    def test_name_entering_is_enabled(self):
        """
                Used role is Admin

                Test  is the field 'name' enabled
                :return:

                  """
        field_name_of_group = self.group_page.WindowCreatingGroup(). \
            field_group_name_get()
        self.assertTrue(field_name_of_group.is_enabled())

    def test_select_direction_is_enabled(self):
        """
                Used role is Admin

                Test  is the field 'direction' enabled
                :return:

                  """

        field_direction = self.group_page.WindowCreatingGroup(). \
            direction_of_group_get()
        self.assertTrue(field_direction.is_enabled())

    def test_select_location_is_enabled_for_admin(self):
        """
                Used role is Admin

                Test  is the field 'location' enabled
                :return:

                  """
        field_location = self.group_page.WindowCreatingGroup(). \
            location_of_group_get()
        self.assertTrue(field_location.is_enabled())

    def test_select_direction_is_enabled_for_coordinator(self):
        """
                Used role is Coordinator

                Test  is the field 'direction' enabled
                :return:

                  """
        field_direction = self.group_page.WindowCreatingGroup(). \
            direction_of_group_get()
        self.assertTrue(field_direction.is_enabled())

    def test_select_location_is_enabled_for_coordinator(self):
        """
                Used role is Coordinator

                Test  is the field 'location' enabled
                :return:

                  """
        field_location = self.group_page.WindowCreatingGroup(). \
            location_of_group_get()
        self.assertTrue(field_location.is_enabled())

    def test_select_location_is_enabled_for_coordinatr(self):
        """
        Try to create a group with empty field 'group name'
        :return:
        """
        self.group_page.WindowCreatingGroup().field_group_name_set(TEST_TOO_LONG_GROUP_NAME)
        self.group_page.WindowCreatingGroup().submit_group_creating()
        self.group_page.WindowCreatingGroup().warning_message_gets()
