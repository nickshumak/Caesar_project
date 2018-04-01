from caesar_items.locators.locators import CreateGroupWindowLocators
from resource.constants_creating_group import TEST_TOO_LONG_GROUP_NAME, \
    MESSAGE_NAME_IS_MORE_20_CHAR, MESSAGE_PLEASE_ENTER_THE_GROUP_NAME, \
    MESSAGE_DIRECTION_IS_NOT_SELECTED, \
    MESSAGE_START_DATE_FIELD_IS_EMPTY, APP_TITLE
from resource.users_base import first_admin
from tests.test_base import TestBase


class TestCreatingGroup(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)
        self.left_menu = self.group_page.open_left_menu()
        self.left_menu.create_group_button().click()

    def test01_name_entering_is_enabled(self):
        """
                Test  is the field 'name' enabled
                :return:

                  """
        field_name_of_group = self.group_page.CreateGroupWindow(). \
            field_group_name_get()
        self.assertTrue(field_name_of_group.is_enabled())

    def test02_select_direction_is_enabled(self):
        """
                Test  is the field 'direction' enabled
                :return:

                  """

        field_direction = self.group_page.CreateGroupWindow(). \
            direction_of_group_get()
        self.assertTrue(field_direction.is_enabled())

    def test03_select_location_is_enabled(self):
        """
                Test  is the field 'location' enabled
                :return:

                  """
        field_location = self.group_page.CreateGroupWindow(). \
            location_of_group_get()
        self.assertTrue(field_location.is_enabled())

    def test04_button_add_teacher_is_enabled(self):
        """
                Test  is the field 'direction' enabled
                :return:

                  """
        button_add_teacher = self.group_page.CreateGroupWindow(). \
            button_teacher_add_get()
        self.assertTrue(button_add_teacher.is_enabled())

    def test0111(self):
        self.group_page.CreateGroupWindow().auto_fill_all_fields()
        self.assertEqual(self.group_page.get_title_name(), APP_TITLE)

    def test06_cancel_button_is_enabled(self):
        cancel_button = self.group_page.CreateGroupWindow().cancel_button_get()
        self.assertTrue(cancel_button.is_enabled())

    def test05_selecting_teacher_is_enabled(self):
        """
                Test  is the field 'location' enabled
                :return:

                  """
        button_add_teacher = self.group_page.CreateGroupWindow(). \
            button_teacher_add_get()
        button_add_teacher.click()
        drop_list_teachers = self.group_page.CreateGroupWindow(). \
            drop_list_teacher_get()
        self.assertTrue(drop_list_teachers.is_enabled())

    def test06_create_group_with_more_20_char_name(self):
        """
        Try to create a group with more than 20 characters 'group name'
        :return:
        """
        self.group_page.CreateGroupWindow().field_group_name_set(
            TEST_TOO_LONG_GROUP_NAME)
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        form_group_name_locator = CreateGroupWindowLocators.GROUP_NAME_FORM
        warning_message = self.group_page.CreateGroupWindow(). \
            warning_message_get_by_locator(form_group_name_locator)
        self.assertEqual(warning_message, MESSAGE_NAME_IS_MORE_20_CHAR)

    def test_create_group_with_empty_field_group_name(self):
        """
        Try to create a group with empty field 'group name'
        :return:
        """
        self.group_page.CreateGroupWindow().field_group_name_set('')
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        form_group_name_locator = CreateGroupWindowLocators.GROUP_NAME_FORM
        warning_message = self.group_page.CreateGroupWindow(). \
            warning_message_get_by_locator(form_group_name_locator)
        self.assertEqual(warning_message, MESSAGE_PLEASE_ENTER_THE_GROUP_NAME)

    def test_create_group_with_empty_field_direction(self):
        """
        Try to create a group with empty field 'group name'
        :return:
        """
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        locator_of_direction_form = CreateGroupWindowLocators.DIRECTION_FORM
        warning_message = self.group_page.CreateGroupWindow(). \
            warning_message_get_by_locator(locator_of_direction_form)
        self.assertEqual(warning_message, MESSAGE_DIRECTION_IS_NOT_SELECTED)

    def test_create_group_with_empty_start_date(self):
        """
        Try to create a group with empty field 'group name'
        :return:
        """
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        locator_of_start_date_form = CreateGroupWindowLocators.START_DATE_FIELD
        warning_message = self.group_page.CreateGroupWindow(). \
            warning_message_get_by_locator(locator_of_start_date_form)
        self.assertEqual(warning_message, MESSAGE_START_DATE_FIELD_IS_EMPTY)
