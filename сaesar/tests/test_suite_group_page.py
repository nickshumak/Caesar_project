import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException,\
    NoSuchElementException

from resource.path_driver import GetDriver
from resource.users_base import *
from resource.url_site import PathUrl
from caesar_items.pages.login_page import LogInPage
from tests.test_base import TestBase


expected_url = 'http://localhost:3000/Groups/Dnipro'
expected_login_page_title = 'Log in - Caesar'
group_name = 'DP-093-JS'
group_to_delete_name = 'DP-098-JS'


class TestGroupPageAdmin(TestBase):
    @classmethod
    def setUpClass(cls):
        """ Create test group to delete."""
        driver = webdriver.Chrome(
            executable_path=GetDriver().CHROME_DRIVER)
        driver.get(PathUrl().SITE_URL)
        driver.maximize_window()
        login_page = LogInPage(driver)
        group_page = login_page.auto_login(first_admin)
        left_menu = group_page.open_left_menu()
        left_menu.create_group_button().click()
        group_page.CreateGroupWindow().auto_fill_all_fields(
            group_to_delete_name, first_admin.location)
        driver.quit()

    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)

    def test01_logout_top_menu(self):
        """ Logout from site using logout button on top menu."""
        top_menu = self.group_page.open_top_menu()
        top_menu.click_logout_button()
        self.assertEqual(self.login_page.get_title_name(),
                         expected_login_page_title)

    def test02_logout_right_menu(self):
        """ Logout from site using logout button on right menu."""
        right_menu = self.group_page.open_right_menu()
        right_menu.click_logout_button()
        self.assertEqual(self.login_page.get_title_name(),
                         expected_login_page_title)

    def test03_open_about(self):
        """ Open about page and check url."""
        expected_page_url = 'http://localhost:3000/About'
        top_menu = self.group_page.open_top_menu()
        top_menu.click_about_button()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test04_open_add(self):
        """ Open add page and check url."""
        expected_page_url = 'http://localhost:3000/Add'
        top_menu = self.group_page.open_top_menu()
        top_menu.click_add_button()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test05_open_schedule(self):
        """ Open schedule page and check url."""
        expected_page_url = 'http://localhost:3000/Schedule/' \
                            + first_admin.location
        top_menu = self.group_page.open_top_menu()
        top_menu.click_schedule_button()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test06_open_students(self):
        """ Open students page and check url."""
        top_menu = self.group_page.open_top_menu()
        top_menu.click_students_button()
        expected_page_url = 'http://localhost:3000/Students/' \
                            + first_admin.location
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test07_open_groups(self):
        """ Open group page and check url."""
        expected_page_url = 'http://localhost:3000/Groups/' \
                            + first_admin.location
        top_menu = self.group_page.open_top_menu()
        top_menu.click_groups_button()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test08_open_locations(self):
        """ Open location panel and check url."""
        expected_page_url = 'http://localhost:3000/Groups/' \
                            + first_admin.location + '/locations'
        top_menu = self.group_page.open_top_menu()
        top_menu.click_locations_button()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test09_open_create_page(self):
        """ Open create group panel and check url."""
        expected_page_url = 'http://localhost:3000/Groups/' \
                            + first_admin.location + '/new'
        left_menu = self.group_page.open_left_menu()
        left_menu.create_group_button().click()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test10_open_edit_group_left_menu(self):
        """ Open edit group panel and check url."""
        expected_page_url = 'http://localhost:3000/Groups/Dnipro/' \
                            + group_name + '/info/edit'
        self.group_page.select_group_by_name(group_name)
        left_menu = self.group_page.open_left_menu()
        left_menu.edit_group_button().click()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test11_open_search_panel_left_menu(self):
        """ Open search panel and check url."""
        search_group_url = 'http://localhost:3000/Groups/Dnipro/' \
                           + group_name + '/Search'
        left_menu = self.group_page.open_left_menu()
        left_menu.search_group_button().click()
        self.assertEqual(self.group_page.get_current_url(), search_group_url)

    def test12_delete_group_left_menu(self):
        """ Check that admin can delete group."""
        expected_string = "group not exist"
        self.group_page.button_boarding_groups().click()
        self.group_page.select_group_by_name(group_to_delete_name)
        left_menu = self.group_page.open_left_menu()
        left_menu.delete_group_button().click()
        self.group_page.confirm_deletion_button().click()
        self.assertEqual(self.group_page.select_group_by_name(
            group_to_delete_name), expected_string)

    def test13_groups_stage_in_progress_or_offering(self):
        """ Check that groups placed in page with right stage status."""
        expected_result = ['in-process', 'offering']
        self.group_page.current_groups_button().click()
        groups_in_current_stage = ('DP-093-JS', 'DP-094-MQC')
        for group in groups_in_current_stage:
            self.group_page.select_group_by_name(group)
            actual_result = self.group_page.get_group_stage_text()
            self.assertIn(actual_result, expected_result)

    def test14_groups_stage_finished(self):
        """ Check that groups placed in page with right stage status."""
        expected_result = 'finished'
        groups_in_ended_stage = ('DP-092-NET', 'DP-065-AQC', 'DP-027-JS')
        self.group_page.ended_groups_button().click()
        for group in groups_in_ended_stage:
            self.group_page.select_group_by_name(group)
            actual_result = self.group_page.get_group_stage_text()
            self.assertEqual(actual_result, expected_result)

    def test15_groups_stage_boarding(self):
        """ Check that groups placed in page with right stage status."""
        expected_result = ('boarding', 'planned')
        groups_in_boarding_stage = ('DP-097-QC', 'DP-095-JS')
        self.group_page.button_boarding_groups().click()
        for group in groups_in_boarding_stage:
            self.group_page.select_group_by_name(group)
            actual_result = self.group_page.get_group_stage_text()
            self.assertIn(actual_result, expected_result)

    def test16_open_edit_user_panel(self):
        """ Check that user can open edit profile panel."""
        expected_result = 'http://localhost:3000/EditProfile'
        right_menu = self.group_page.open_right_menu()
        right_menu.click_edit_user_button()
        self.assertEqual(right_menu.get_current_url(), expected_result)

    def test17_open_groups_info_panel(self):
        """ Check that user can open info panel in selected group."""
        expected_result = 'http://localhost:3000/Groups/Dnipro/' \
                          + group_name + '/info'
        self.group_page.select_group_by_name(group_name)
        self.group_page.group_info_button().click()
        self.assertEqual(self.group_page.get_current_url(), expected_result)

    def test18_open_groups_students_panel(self):
        """ Check that user can open students panel in selected group."""
        expected_result = 'http://localhost:3000/Groups/Dnipro/' \
                          + group_name + '/students'
        self.group_page.select_group_by_name(group_name)
        self.group_page.group_students_button().click()
        self.assertEqual(self.group_page.get_current_url(), expected_result)

    def test19_open_groups_schedule_panel(self):
        """ Check that user can open schedule panel in selected group."""
        expected_result = 'http://localhost:3000/Groups/Dnipro/' \
                          + group_name + '/shedule'
        self.group_page.select_group_by_name(group_name)
        self.group_page.group_calendar_button().click()
        self.assertEqual(self.group_page.get_current_url(), expected_result)

    def test20_open_groups_message_panel(self):
        """ Check that user can open messages panel in selected group."""
        expected_result = 'http://localhost:3000/Groups/Dnipro/' \
                          + group_name + '/message'
        self.group_page.select_group_by_name(group_name)
        self.group_page.group_message_button().click()
        self.assertEqual(self.group_page.get_current_url(), expected_result)

    def test21_open_edit_group_from_info_panel(self):
        """ Check that user can open edit group panel in selected group."""
        expected_result = 'http://localhost:3000/Groups/Dnipro/' \
                          + group_name + '/info/edit'
        self.group_page.select_group_by_name(group_name)
        self.group_page.group_edit_button().click()
        self.assertEqual(self.group_page.get_current_url(), expected_result)


class TestGroupPageCoordinator(TestBase):
    @classmethod
    def setUpClass(cls):
        """ Create group to delete in 25th test."""
        driver = webdriver.Chrome(
            executable_path=GetDriver().CHROME_DRIVER)
        driver.get(PathUrl().SITE_URL)
        driver.maximize_window()
        login_page = LogInPage(driver)
        group_page = login_page.auto_login(first_admin)
        left_menu = group_page.open_left_menu()
        left_menu.create_group_button().click()
        group_page.CreateGroupWindow().auto_fill_all_fields(
            group_to_delete_name, first_admin.location)
        driver.quit()

    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(coordinator)

    def test22_open_create_page(self):
        """ Open create group panel as coordinator and check url."""
        left_menu = self.group_page.open_left_menu()
        left_menu.create_group_button().click()
        expected_page_url = 'http://localhost:3000/Groups/' \
                            + coordinator.location + '/new'
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test23_open_edit_group_left_menu(self):
        """ Open edit group panel as coordinator and check url."""
        edit_group_url = 'http://localhost:3000/Groups/Dnipro/' \
                         + group_name + '/info/edit'
        self.group_page.select_group_by_name(group_name)
        left_menu = self.group_page.open_left_menu()
        left_menu.edit_group_button().click()
        self.assertEqual(self.group_page.get_current_url(), edit_group_url)

    def test24_open_search_panel_left_menu(self):
        """ Open search panel and check url."""
        edit_group_url = 'http://localhost:3000/Groups/Dnipro/' \
                         + group_name + '/Search'
        left_menu = self.group_page.open_left_menu()
        left_menu.search_group_button().click()
        self.assertEqual(self.group_page.get_current_url(), edit_group_url)

    def test25_delete_group_left_menu(self):
        """ Check that coordinator can delete group."""
        expected_string = "group not exist"
        self.group_page.button_boarding_groups().click()
        self.group_page.select_group_by_name(group_to_delete_name)
        left_menu = self.group_page.open_left_menu()
        left_menu.delete_group_button().click()
        self.group_page.confirm_deletion_button().click()
        self.assertEqual(self.group_page.select_group_by_name(
            group_to_delete_name), expected_string)


class TestGroupPageTeacher(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(teacher)

    def test26_disabled_create_button_for_teacher(self):
        """ Check that teacher doesn't have create button."""
        left_menu = self.group_page.open_left_menu()
        self.assertRaises(TimeoutException, left_menu.create_group_button)

    def test27_delete_button_disabled_for_teacher(self):
        """ Check that teacher doesn't have delete button."""
        self.group_page.select_group_by_name(group_name)
        left_menu = self.group_page.open_left_menu()
        self.assertRaises(NoSuchElementException, left_menu.
                          delete_group_button)

    def test28_left_menu_edit_button_disabled_for_teacher(self):
        """ Check that teacher doesn't have edit button."""
        self.group_page.select_group_by_name(group_name)
        left_menu = self.group_page.open_left_menu()
        self.assertRaises(NoSuchElementException, left_menu.edit_group_button)

    def test29_open_search_panel_left_menu(self):
        """ Open search panel and check url."""
        edit_group_url = 'http://localhost:3000/Groups/Dnipro/' \
                         + group_name + '/Search'
        left_menu = self.group_page.open_left_menu()
        left_menu.search_group_button()
        self.assertEqual(self.group_page.get_current_url(), edit_group_url)


if __name__ == '__main__':
    unittest.main()
