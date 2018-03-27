from front.pages.login_page import LogInPage
import unittest
from resource.users_base import *
from tests.test_base import TestBase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver

expected_message = 'Incorrect login or password. Please, try again'
expected_page_title = 'Caesar'


class TestLoginPage(TestBase):
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = webdriver.Chrome(
    #         executable_path=GetDriver().DRIVER_CHROME)
    #     cls.driver.get(PathUrl().URL_SITE)
    #     cls.login_page = LogInPage(cls.driver)
    #     cls.login_page.enter_login(first_admin.login)
    #     cls.login_page.enter_password(first_admin.password)
    #     cls.login_page.submit()
    #     create_8_users_for_tests(cls.driver)

    def test01_submit_button_enabled(self):
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.assertTrue(self.login_page.submit_button_element().is_enabled())

    def test02_sign_in_as_admin(self):
        self.login_page.enter_login(first_admin.login)
        self.login_page.enter_password(first_admin.password)
        self.login_page.submit()
        group_page = GroupsPage(self.driver)
        self.assertEqual(self.driver.title, expected_page_title)
        right_bar = group_page.right_menu_open()
        self.assertEqual(right_bar.user_full_name(), first_admin.full_name)
        self.assertEqual(right_bar.user_role(), first_admin.role)

    def test03_sign_in_as_coordinator(self):
        self.login_page.enter_login(coordinator.login)
        self.login_page.enter_password(coordinator.password)
        self.login_page.submit()
        group_page = GroupsPage(self.driver)
        self.assertEqual(self.driver.title, expected_page_title)
        right_bar = group_page.right_menu_open()
        self.assertEqual(right_bar.user_full_name(), coordinator.full_name)
        self.assertEqual(right_bar.user_role(), coordinator.role)

    def test04_sign_in_as_teacher(self):
        self.login_page.enter_login(teacher.login)
        self.login_page.enter_password(teacher.password)
        self.login_page.submit()
        group_page = GroupsPage(self.driver)
        self.assertEqual(self.driver.title, expected_page_title)
        right_bar = group_page.right_menu_open()
        self.assertEqual(right_bar.user_full_name(), teacher.full_name)
        self.assertEqual(right_bar.user_role(), teacher.role)

    def test05_length_password_equal_4(self):
        self.login_page.enter_login(user_password_length_4.login)
        self.login_page.enter_password(user_password_length_4.password)
        self.login_page.submit()
        self.assertEqual(self.driver.title, expected_page_title)

    def test06_length_password_equal_10(self):
        self.login_page.enter_login(user_password_length_10.login)
        self.login_page.enter_password(user_password_length_10.password)
        self.login_page.submit()
        self.assertEqual(self.driver.title, expected_page_title)

    def test07_length_login_equal_4(self):
        self.login_page.enter_login(user_login_length_4.login)
        self.login_page.enter_password(user_login_length_4.password)
        self.login_page.submit()
        self.assertEqual(self.driver.title, expected_page_title)

    def test08_length_login_equal_10(self):
        self.login_page.enter_login(user_login_length_10.login)
        self.login_page.enter_password(user_login_length_10.password)
        self.login_page.submit()
        self.assertEqual(self.driver.title, expected_page_title)

    def test09_auto_login_function(self):
        self.login_page.auto_login(first_admin)
        self.assertEqual(self.driver.title, expected_page_title)

    def test10_sensitive_to_case(self):
        self.login_page.enter_login(first_admin.login.upper())
        self.login_page.enter_password(first_admin.password.upper())
        self.login_page.submit()
        self.assertEqual(self.driver.title, expected_page_title)

    def test11_enter_tab_buttons(self):
        ActionChains(self.driver).send_keys(first_admin.login).send_keys(Keys.TAB)\
            .send_keys(first_admin.password).send_keys(Keys.ENTER).perform()
        time.sleep(1)
        self.assertEqual(self.driver.title, expected_page_title)

    # negative tests
    def test12_submit_button_is_disabled(self):
        for step in range(3):
            if step == 0:
                self.login_page.enter_login(first_admin.login)
                self.login_page.enter_password()
            elif step == 1:
                self.login_page.enter_login()
                self.login_page.enter_password(first_admin.password)
            elif step == 2:
                self.login_page.enter_password()
            self.assertFalse(self.login_page.submit_button_element().is_enabled())

    def test13_length_login_equal_3(self):
        self.login_page.enter_login(user_login_length_3.login)
        self.login_page.enter_password(user_login_length_3.password)
        self.login_page.submit()
        self.assertEqual(self.login_page.message(), expected_message)

    def test14_length_login_equal_11(self):
        self.login_page.enter_login(user_login_length_11.login)
        self.login_page.enter_password(user_login_length_11.password)
        self.login_page.submit()
        self.assertEqual(self.login_page.message(), expected_message)

    def test15_length_password_equal_3(self):
        self.login_page.enter_login(user_password_length_3.login)
        self.login_page.enter_password(user_password_length_3.password)
        self.login_page.submit()
        self.assertEqual(self.login_page.message(), expected_message)

    def test16_length_password_equal_11(self):
        self.login_page.enter_login(user_password_length_11.login)
        self.login_page.enter_password(user_password_length_11.password)
        self.login_page.submit()
        self.assertEqual(self.login_page.message(), expected_message)


if __name__ == '__main__':
    unittest.main()
