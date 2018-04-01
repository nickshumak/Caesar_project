import unittest
from resource.users_base import *
from tests.test_base import TestBase

expected_url = 'http://localhost:3000/Groups/Dnipro'
expected_login_page_title = 'Log in - Caesar'
group_name = 'DP-093-JS'
group_to_delete_name = ''


class TestGroupPageAdmin(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(first_admin)

    def test01_logout_top_menu(self):
        """
        logout from site using logout button on top menu
        """
        top_menu = self.group_page.open_top_menu()
        top_menu.click_logout_button()
        self.assertEqual(self.login_page.get_title_name(),
                         expected_login_page_title)

    def test02_logout_right_menu(self):
        """
        logout from site using logout button on right menu
        """
        right_menu = self.group_page.open_right_menu()
        right_menu.click_logout_button()
        self.assertEqual(self.login_page.get_title_name(),
                         expected_login_page_title)

    def test03_open_about(self):
        """
        open about page and check url
        """
        expected_page_url = 'http://localhost:3000/About'
        top_menu = self.group_page.open_top_menu()
        top_menu.click_about_button()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test04_open_add(self):
        """
        open add page and check url
        """
        expected_page_url = 'http://localhost:3000/Add'
        top_menu = self.group_page.open_top_menu()
        top_menu.click_add_button()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test05_open_schedule(self):
        """
        open schedule page and check url
        """
        expected_page_url = 'http://localhost:3000/Schedule/' \
                            + first_admin.location
        top_menu = self.group_page.open_top_menu()
        top_menu.click_schedule_button()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test06_open_students(self):
        """
        open students page and check url
        """
        top_menu = self.group_page.open_top_menu()
        top_menu.click_students_button()
        expected_page_url = 'http://localhost:3000/Students/' \
                            + first_admin.location
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test07_open_groups(self):
        """
        open group page and check url
        """
        expected_page_url = 'http://localhost:3000/Groups/' \
                            + first_admin.location
        top_menu = self.group_page.open_top_menu()
        top_menu.click_groups_button()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test08_open_locations(self):
        """
        open location panel and check url
        """
        expected_page_url = 'http://localhost:3000/Groups/' \
                            + first_admin.location + '/locations'
        top_menu = self.group_page.open_top_menu()
        top_menu.click_locations_button()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test09_open_create_page(self):
        """
        open create group panel and check url
        """
        expected_page_url = 'http://localhost:3000/Groups/' \
                            + first_admin.location + '/new'
        left_menu = self.group_page.open_left_menu()
        left_menu.create_group_button().click()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test10_open_edit_group_left_menu(self):
        """
        open edit group panel and check url
        """
        expected_page_url = 'http://localhost:3000/Groups/Dnipro/' \
                            + group_name + '/info/edit'
        self.group_page.select_group_by_name(group_name)
        left_menu = self.group_page.open_left_menu()
        left_menu.edit_group_button().click()
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test11_open_search_panel_left_menu(self):
        """
        open search panel and check url
        """
        search_group_url = 'http://localhost:3000/Groups/Dnipro/' \
                           + group_name + '/Search'
        left_menu = self.group_page.open_left_menu()
        left_menu.search_group_button().click()
        self.assertEqual(self.group_page.get_current_url(), search_group_url)

    def test12_delete_group_left_menu(self):
        """
        check that admin can delete group
        """
        edit_group_url = 'http://localhost:3000/Groups/Dnipro/' \
                         + group_name + '/Search'
        self.group_page.select_group_by_name(group_to_delete_name)
        left_menu = self.group_page.open_left_menu()
        # left_menu.delete_group_button().click()

    def test13_groups_stage_in_progress_or_offering(self):
        """
        check that groups placed in page with right stage status
        """
        expected_result = ['in-process', 'offering']
        self.group_page.current_groups_button().click()
        groups_in_current_stage = ('DP-093-JS', 'DP-094-MQC')
        for group in groups_in_current_stage:
            self.group_page.select_group_by_name(group)
            actual_result = self.group_page.get_group_stage_text()
            self.assertIn(actual_result, expected_result)

    def test14_groups_stage_finished(self):
        """
        check that groups placed in page with right stage status
        """
        expected_result = 'finished'
        self.group_page.ended_groups_button().click()
        groups_in_ended_stage = ('DP-092-NET', 'DP-065-AQC', 'DP-027-JS')
        for group in groups_in_ended_stage:
            self.group_page.select_group_by_name(group)
            actual_result = self.group_page.get_group_stage_text()
            self.assertEqual(actual_result, expected_result)

    def test15_groups_stage_boarding(self):
        """
        check that groups placed in page with right stage status
        """
        expected_result = 'boarding'
        self.group_page.button_boarding_groups().click()
        groups_in_boarding_stage = ('DP-097-QC', 'DP-095-JS')
        for group in groups_in_boarding_stage:
            self.group_page.select_group_by_name(group)
            actual_result = self.group_page.get_group_stage_text()
            self.assertEqual(actual_result, expected_result)


class TestGroupPageCoordinator(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(coordinator)

    def test16_open_create_page(self):
        """
        open create group panel as coordinator and check url
        """
        left_menu = self.group_page.open_left_menu()
        left_menu.create_group_button().click()
        expected_page_url = 'http://localhost:3000/Groups/' \
                            + coordinator.location + '/new'
        self.assertEqual(self.group_page.get_current_url(), expected_page_url)

    def test17_open_edit_group_left_menu(self):
        """
        open edit group panel as coordinator and check url
        """
        edit_group_url = 'http://localhost:3000/Groups/Dnipro/' \
                         + group_name + '/info/edit'
        self.group_page.select_group_by_name(group_name)
        left_menu = self.group_page.open_left_menu()
        left_menu.edit_group_button().click()
        self.assertEqual(self.group_page.get_current_url(), edit_group_url)

    def test18_open_search_panel_left_menu(self):
        """
        open search panel and check url
        """
        edit_group_url = 'http://localhost:3000/Groups/Dnipro/' \
                         + group_name + '/Search'
        left_menu = self.group_page.open_left_menu()
        left_menu.search_group_button().click()
        self.assertEqual(self.group_page.get_current_url(), edit_group_url)

    def test19_delete_group_left_menu(self):
        """
        check that coordinator can delete group
        """
        edit_group_url = 'http://localhost:3000/Groups/Dnipro/' \
                         + group_name + '/Search'
        self.group_page.select_group_by_name(group_to_delete_name)
        left_menu = self.group_page.open_left_menu()
        # left_menu.delete_group_button().click()
        # self.assertEqual(self.group_page.get_current_url(), edit_group_url)


class TestGroupPageTeacher(TestBase):
    def setUp(self):
        super().setUp()
        self.group_page = self.login_page.auto_login(teacher)

    def test20_disabled_create_button_for_teacher(self):
        """
        Check that teacher doen't have create button
        """
        left_menu = self.group_page.open_left_menu()
        self.assertRaises(NoSuchElementException, left_menu.create_group_button)

    def test21_delete_button_disabled_for_teacher(self):
        """
        Check that teacher doen't have delete button
        """
        self.group_page.select_group_by_name(group_name)
        left_menu = self.group_page.open_left_menu()
        self.assertRaises(NoSuchElementException, left_menu.delete_group_button)

    def test22_left_menu_edit_button_disabled_for_teacher(self):
        """
        Check that teacher doen't have edit button
        """
        self.group_page.select_group_by_name(group_name)
        left_menu = self.group_page.open_left_menu()
        self.assertRaises(NoSuchElementException, left_menu.edit_group_button)

    def test23_open_search_panel_left_menu(self):
        """
        open search panel and check url
        """
        edit_group_url = 'http://localhost:3000/Groups/Dnipro/' \
                         + group_name + '/Search'
        left_menu = self.group_page.open_left_menu()
        left_menu.search_group_button()
        self.assertEqual(self.group_page.get_current_url(), edit_group_url)


if __name__ == '__main__':
    unittest.main()
