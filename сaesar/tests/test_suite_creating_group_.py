from resource.constants_creating_group import TEST_TOO_LONG_GROUP_NAME, \
    MESSAGE_NAME_IS_MORE_20_CHAR, MESSAGE_PLEASE_ENTER_THE_GROUP_NAME, \
    MESSAGE_DIRECTION_IS_NOT_SELECTED, \
    MESSAGE_START_DATE_FIELD_IS_EMPTY, APP_TITLE, TEST_GROUP_NAME, \
    TEXT_ITERATIONS, MESSAGE_EMPTY_EXPERT_NAME, TEST_SECOND_EXPERT_NAME, \
    MESSAGE_INVALID_EXPERT_NAME, TEST_FIRST_EXPERT_NAME, TEST_THIRD_EXPERT_NAME
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
            get_group_name_field()
        self.assertTrue(field_name_of_group.is_enabled())

    def test02_select_direction_is_enabled(self):
        """
                Test  is the field 'direction' enabled
                :return:
                  """

        field_direction = self.group_page.CreateGroupWindow(). \
            get_group_direction()
        self.assertTrue(field_direction.is_enabled())

    def test03_select_location_is_enabled(self):
        """
                Test  is the field 'location' enabled
                :return:
                  """
        field_location = self.group_page.CreateGroupWindow(). \
            get_group_location()
        self.assertTrue(field_location.is_enabled())

    def test04_adding_more_20_teachers(self):
        """
                Test  is the field 'direction' enabled
                :return:
                  """
        i = TEXT_ITERATIONS
        while i > 0:
            self.group_page.CreateGroupWindow().add_teacher()
            i -= 1
        teachers_list = self.group_page.CreateGroupWindow().get_added_teachers_list()
        self.assertNotEqual(len(teachers_list), len(set(teachers_list)))

    def test05_save_button_is_enabled(self):
        save_button = self.group_page.CreateGroupWindow().get_save_group_button()
        self.assertTrue(save_button.is_enabled)

    def test06_save_button_is_working(self):
        self.group_page.CreateGroupWindow().auto_fill_all_fields(TEST_GROUP_NAME)
        self.assertEqual(self.group_page.get_title_name(), APP_TITLE)

    def test07_cancel_button_is_enabled(self):
        cancel_button = self.group_page.CreateGroupWindow().cancel_button_get()
        self.assertTrue(cancel_button.is_enabled())

    def test08_cancel_button_is_working(self):
        cancel_button = self.group_page.CreateGroupWindow().cancel_button_get()
        cancel_button.click()
        self.assertEqual(self.group_page.get_title_name(), APP_TITLE)

    def test09_create_group_with_more_20_char_name(self):
        """
        Try to create a group with more than 20 characters 'group name'
        :return:
        """
        self.group_page.CreateGroupWindow().set_group_name(
            TEST_TOO_LONG_GROUP_NAME)
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        form_group_name = self.group_page.CreateGroupWindow().get_group_name_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(form_group_name)
        self.assertEqual(warning_message, MESSAGE_NAME_IS_MORE_20_CHAR)

    def test10_create_group_with_empty_field_group_name(self):
        """
        Try to create a group with empty field 'group name'
        :return:
        """
        self.group_page.CreateGroupWindow().set_group_name('')
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        form_group_name = self.group_page.CreateGroupWindow().get_group_name_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(form_group_name)
        self.assertEqual(warning_message, MESSAGE_PLEASE_ENTER_THE_GROUP_NAME)

    def test11_create_group_with_empty_field_direction(self):
        """
        Try to create a group with empty field 'group name'
        :return:
        """
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        direction_form = self.group_page.CreateGroupWindow().get_group_direction_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(direction_form)
        self.assertEqual(warning_message, MESSAGE_DIRECTION_IS_NOT_SELECTED)

    def test12_create_group_with_empty_start_date(self):
        """
        Try to create a group with empty field 'group name'
        :return:
        """
        self.group_page.CreateGroupWindow().submit_group_creating_button()
        start_date_form = self.group_page.CreateGroupWindow().get_start_date_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(start_date_form)
        self.assertEqual(warning_message, MESSAGE_START_DATE_FIELD_IS_EMPTY)

    def test13_add_expert_without_name(self):
        self.group_page.CreateGroupWindow().add_expert('')
        expert_form = self.group_page.CreateGroupWindow().get_experts_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(expert_form)
        self.assertEqual(warning_message, MESSAGE_EMPTY_EXPERT_NAME)

    def test14_add_expert_non_valid_name(self):
        self.group_page.CreateGroupWindow().add_expert(TEST_SECOND_EXPERT_NAME)
        expert_form = self.group_page.CreateGroupWindow().get_experts_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(expert_form)
        self.assertEqual(warning_message, MESSAGE_INVALID_EXPERT_NAME)

    def test15_adding_more_20_same_expert(self):
        """
                Test  is the field 'direction' enabled
                :return:
                  """
        i = TEXT_ITERATIONS
        while i > 0:
            self.group_page.CreateGroupWindow().add_expert(TEST_THIRD_EXPERT_NAME)
            i -= 1
        experts_list = self.group_page.CreateGroupWindow().get_added_experts_list()
        self.assertNotEqual(len(experts_list), len(set(experts_list)))

    def test16_add_expert_empty_name(self):
        self.group_page.CreateGroupWindow().add_expert(TEST_THIRD_EXPERT_NAME)
        expert_form = self.group_page.CreateGroupWindow().get_experts_form()
        warning_message = self.group_page.CreateGroupWindow(). \
            get_warning_message_by_form(expert_form)
        self.assertNotEqual(warning_message, MESSAGE_INVALID_EXPERT_NAME)
