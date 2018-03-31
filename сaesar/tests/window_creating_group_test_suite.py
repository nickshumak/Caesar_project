from caesar_items.locators.locators import WindowCreateGroup
from constants.for_window_creating_group import TEST_TOO_LONG_GROUP_NAME, \
    MESSAGE_NAME_IS_MORE_20_CHAR, MESSAGE_PLEASE_ENTER_THE_GROUP_NAME, MESSAGE_DIRECTION_IS_NOT_SELECTED
from resource.users_base import first_admin
from tests.test_base import TestBase


class TestCreatingGroup(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)
        self.left_menu = self.group_page.open_left_menu()
        self.left_menu.create_group().click()

    def test_name_entering_is_enabled(self):
        """
                Test  is the field 'name' enabled
                :return:

                  """
        field_name_of_group = self.group_page.WindowCreatingGroup(). \
            field_group_name_get()
        self.assertTrue(field_name_of_group.is_enabled())

    def test_select_direction_is_enabled(self):
        """
                Test  is the field 'direction' enabled
                :return:

                  """

        field_direction = self.group_page.WindowCreatingGroup(). \
            direction_of_group_get()
        self.assertTrue(field_direction.is_enabled())

    def test_select_location_is_enabled_for_admin(self):
        """
                Test  is the field 'location' enabled
                :return:

                  """
        field_location = self.group_page.WindowCreatingGroup(). \
            location_of_group_get()
        self.assertTrue(field_location.is_enabled())

    def test_select_direction_is_enabled_for_coordinator(self):
        """
                Test  is the field 'direction' enabled
                :return:

                  """
        field_direction = self.group_page.WindowCreatingGroup(). \
            direction_of_group_get()
        self.assertTrue(field_direction.is_enabled())

    def test_select_location_is_enabled_for_coordinator(self):
        """
                Test  is the field 'location' enabled
                :return:

                  """
        field_location = self.group_page.WindowCreatingGroup(). \
            location_of_group_get()
        self.assertTrue(field_location.is_enabled())

    def test_create_group_with_more_20_char_name(self):
        """
        Try to create a group with more than 20 characters 'group name'
        :return:
        """
        self.group_page.WindowCreatingGroup().field_group_name_set(TEST_TOO_LONG_GROUP_NAME)
        self.group_page.WindowCreatingGroup().submit_group_creating()
        message = self.group_page.WindowCreatingGroup().warning_message_get()
        self.assertEqual(message, MESSAGE_NAME_IS_MORE_20_CHAR)

    def test_create_group_with_empty_field_group_name(self):
        """
        Try to create a group with empty field 'group name'
        :return:
        """
        self.group_page.WindowCreatingGroup().field_group_name_set('')
        self.group_page.WindowCreatingGroup().submit_group_creating()
        message = self.group_page.WindowCreatingGroup().warning_message_get()
        self.assertEqual(message, MESSAGE_PLEASE_ENTER_THE_GROUP_NAME)

    def test_create_group_with_empty_field_direction(self):
        """
        Try to create a group with empty field 'group name'
        :return:
        """
        self.group_page.WindowCreatingGroup().submit_group_creating()
        locator_of_direction_form = WindowCreateGroup.FORM_DIRECTION
        message = self.group_page.WindowCreatingGroup(). \
            warning_message_get_by_locator(locator_of_direction_form)
        self.assertEqual(message, MESSAGE_DIRECTION_IS_NOT_SELECTED)
