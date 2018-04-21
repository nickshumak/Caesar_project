import unittest
from selenium import webdriver
from resource.users_base import *
from tests.test_base import TestBase
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from caesar_items.pages.login_page import LogInPage
from resource.error_handler import logger_exception


expected_message = 'Incorrect login or password. Please, try again'
expected_page_title = 'Caesar'


class TestLoginPage(TestBase):
    @classmethod
    def setUpClass(cls):
        """ Create 8 users for tests."""
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().CHROME_DRIVER)
        cls.driver.get(PathUrl().SITE_URL)
        cls.login_page = LogInPage(cls.driver)
        cls.login_page.set_login_field_text(first_admin.login)
        cls.login_page.set_password_field_text(first_admin.password)
        cls.group_page = cls.login_page.click_submit_button()
        cls.group_page.open_admin_page()
        create_8_users_for_tests(cls.driver)
        cls.driver.quit()

    @logger_exception
    def test01_submit_button_enabled(self):
        """ Check that button is active when login and password entered."""
        self.login_page.set_login_field_text(first_admin.login)
        self.login_page.set_password_field_text(first_admin.password)
        self.assertTrue(self.login_page.submit_button().is_enabled())

    @logger_exception
    def test02_login_as_admin(self):
        """ Sign in as admin and check his name and role on page."""
        self.login_page.set_login_field_text(first_admin.login)
        self.login_page.set_password_field_text(first_admin.password)
        self.group_page = self.login_page.click_submit_button()
        self.assertEqual(self.group_page.get_title_name(), expected_page_title)
        right_menu = self.group_page.open_right_menu()
        self.assertEqual(right_menu.get_user_full_name_text(),
                         first_admin.full_name)
        self.assertEqual(right_menu.get_user_role_text(), first_admin.role)

    @logger_exception
    def test03_login_as_coordinator(self):
        """ Sign in as coordinator and check his name and role on page."""
        self.login_page.set_login_field_text(coordinator.login)
        self.login_page.set_password_field_text(coordinator.password)
        self.group_page = self.login_page.click_submit_button()
        right_menu = self.group_page.open_right_menu()
        self.assertEqual(right_menu.get_user_full_name_text(), coordinator.full_name)
        self.assertEqual(right_menu.get_user_role_text(), coordinator.role)

    @logger_exception
    def test04_sign_in_as_teacher(self):
        """ Sign in as teacher and check his name and role on page."""
        self.login_page.set_login_field_text(teacher.login)
        self.login_page.set_password_field_text(teacher.password)
        self.group_page = self.login_page.click_submit_button()
        self.assertEqual(self.group_page.get_title_name(), expected_page_title)
        right_menu = self.group_page.open_right_menu()
        self.assertEqual(right_menu.get_user_full_name_text(), teacher.full_name)
        self.assertEqual(right_menu.get_user_role_text(), teacher.role)

    @logger_exception
    def test05_length_password_equal_4(self):
        """ Check that user with password length equal 4 can sign in on site."""
        self.login_page.set_login_field_text(user_password_len_4.login)
        self.login_page.set_password_field_text(user_password_len_4.password)
        self.group_page = self.login_page.click_submit_button()
        self.assertEqual(self.group_page.get_title_name(), expected_page_title)

    @logger_exception
    def test06_length_password_equal_10(self):
        """ Check that user with password length equal 10 can sign in on site."""
        self.login_page.set_login_field_text(user_password_len_10.login)
        self.login_page.set_password_field_text(user_password_len_10.password)
        self.group_page = self.login_page.click_submit_button()
        self.assertEqual(self.group_page.get_title_name(), expected_page_title)

    @logger_exception
    def test07_length_login_equal_4(self):
        """ Check that user with login length equal 4 can sign in on site."""
        self.login_page.set_login_field_text(user_login_len_4.login)
        self.login_page.set_password_field_text(user_login_len_4.password)
        self.group_page = self.login_page.click_submit_button()
        self.assertEqual(self.group_page.get_title_name(), expected_page_title)

    @logger_exception
    def test08_length_login_equal_10(self):
        """ Check that user with password length equal 10 can sign in on site."""
        self.login_page.set_login_field_text(user_login_len_10.login)
        self.login_page.set_password_field_text(user_login_len_10.password)
        self.group_page = self.login_page.click_submit_button()
        self.assertEqual(self.group_page.get_title_name(), expected_page_title)

    @logger_exception
    def test09_sensitive_to_case(self):
        """ Check that upper case of user login and password
        doesn't influence on login to site. """
        self.login_page.set_login_field_text(first_admin.login.upper())
        self.login_page.set_password_field_text(first_admin.password.upper())
        self.group_page = self.login_page.click_submit_button()
        self.assertEqual(self.group_page.get_title_name(), expected_page_title)

    @logger_exception
    def test10_check_enter_n_tab_buttons(self):
        """ Check tab and enter keys:
        tab - go to the next field
        enter - confirm action(login on site)"""
        self.group_page = self.login_page.\
            login_use_tab_n_enter_keys(first_admin)
        self.assertEqual(self.group_page.get_title_name(), expected_page_title)

    # negative tests
    @logger_exception
    def test11_password_field_empty_submit_button_is_disabled(self):
        """ Check if password field is empty, submit button disabled."""
        self.login_page.set_login_field_text(first_admin.login)
        self.login_page.set_password_field_text()
        self.assertFalse(self.login_page.submit_button().is_enabled())

    @logger_exception
    def test12_login_field_empty_submit_button_is_disabled(self):
        """ Check if login field is empty, submit button disabled."""
        self.login_page.set_login_field_text()
        self.login_page.set_password_field_text(first_admin.password)
        self.assertFalse(self.login_page.submit_button().is_enabled())

    @logger_exception
    def test13_all_fields_empty_submit_button_is_disabled(self):
        """ Check if all field is empty, submit button disabled."""
        self.login_page.set_login_field_text()
        self.login_page.set_password_field_text()
        self.assertFalse(self.login_page.submit_button().is_enabled())

    @logger_exception
    def test14_length_login_equal_3(self):
        """ Check that user with login length equal 3 can not sign in on site.
        Error message appears."""
        self.login_page.set_login_field_text(user_login_len_3.login)
        self.login_page.set_password_field_text(user_login_len_3.password)
        self.login_page.click_submit_button()
        self.assertEqual(self.login_page.get_message_text(), expected_message)

    @logger_exception
    def test15_length_login_equal_11(self):
        """ Check that user with login length equal 11 can not sign in on site.
        Error message appears."""
        self.login_page.set_login_field_text(user_login_len_11.login)
        self.login_page.set_password_field_text(user_login_len_11.password)
        self.login_page.click_submit_button()
        self.assertEqual(self.login_page.get_message_text(), expected_message)

    @logger_exception
    def test16_length_password_equal_3(self):
        """ Check that user with password length equal 3 can not sign in on site.
        Error message appears."""
        self.login_page.set_login_field_text(user_password_len_3.login)
        self.login_page.set_password_field_text(user_password_len_3.password)
        self.login_page.click_submit_button()
        self.assertEqual(self.login_page.get_message_text(), expected_message)

    @logger_exception
    def test17_length_password_equal_11(self):
        """ Check that user with password length equal 11 can not sign in on site.
        Error message appears."""
        self.login_page.set_login_field_text(user_password_len_11.login)
        self.login_page.set_password_field_text(user_password_len_11.password)
        self.login_page.click_submit_button()
        self.assertEqual(self.login_page.get_message_text(), expected_message)


if __name__ == '__main__':
    unittest.main()