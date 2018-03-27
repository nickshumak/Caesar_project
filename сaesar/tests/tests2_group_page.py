from resource.users_base import *
from caesar_items.pages.groups_page import GroupsPage
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from caesar_items.pages.login_page import *


import unittest

expected_url = 'http://localhost:3000/Groups/Dnipro'
expected_title_login_page = 'Log in - Caesar'
group_name = 'DP-093-JS'


class TestGroupPageAdmin(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        cls.driver.get(PathUrl().URL_SITE)
        cls.login_page = LogInPage(cls.driver)
        cls.driver.maximize_window()
        cls.login_page.auto_login(first_admin)
        cls.group_page = GroupsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.get('http://localhost:3000/Groups/' + first_admin.location)
        self.driver.implicitly_wait(2)

    def test17_logout_top_menu(self):
        top_menu = self.group_page.top_menu_open()
        top_menu.log_out_click()
        self.assertEqual(self.driver.title, expected_title_login_page)
        self.login_page.auto_login(first_admin)

    def test18_logout_right_menu(self):
        right_menu = self.group_page.right_menu_open()
        login_page = right_menu.log_out_click()
        self.assertEqual(login_page.get_title_name(), expected_title_login_page)
        self.login_page.auto_login(first_admin)

    def test19_open_about(self):
        expected_page_url = 'http://localhost:3000/About'
        top_menu = self.group_page.top_menu_open()
        top_menu.about()
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test20_open_schedule(self):
        expected_page_url = 'http://localhost:3000/Schedule/' + first_admin.location
        top_menu = self.group_page.top_menu_open()
        top_menu.schedule()
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test21_open_students(self):
        top_menu = self.group_page.top_menu_open()
        top_menu.students()
        expected_page_url = 'http://localhost:3000/Students/' + first_admin.location
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test22_open_groups(self):
        expected_page_url = 'http://localhost:3000/Groups/' + first_admin.location
        top_menu = self.group_page.top_menu_open()
        top_menu.groups()
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test23_open_locations(self):
        expected_page_url = 'http://localhost:3000/Groups/' + first_admin.location + '/locations'
        top_menu = self.group_page.top_menu_open()
        top_menu.locations()
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test24_open_create_page(self):
        expected_page_url = 'http://localhost:3000/Groups/' + first_admin.location + '/new'
        left_menu = self.group_page.left_menu_open()
        left_menu.create_group().click()
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test25_open_edit_group_left_menu(self):
        edit_group_url = 'http://localhost:3000/Groups/Dnipro/' + group_name + '/info/edit'
        self.group_page.select_group(group_name)
        left_menu = self.group_page.left_menu_open()
        left_menu.edit_group().click()
        self.assertEqual(self.driver.current_url, edit_group_url)


class TestGroupPageCoordinator(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        cls.driver.get(PathUrl().URL_SITE)
        cls.login_page = LogInPage(cls.driver)
        cls.driver.maximize_window()
        cls.login_page.auto_login(coordinator)
        cls.group_page = GroupsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.get('http://localhost:3000/Groups/Dnipro')

    def test26_open_create_page(self):
        left_menu = self.group_page.left_menu_open()
        left_menu.create_group().click()
        expected_page_url = 'http://localhost:3000/Groups/' + coordinator.location + '/new'
        self.assertEqual(self.driver.current_url, expected_page_url)

    def test27_open_edit_group_left_menu(self):
        edit_group_url = 'http://localhost:3000/Groups/Dnipro/' + group_name + '/info/edit'
        top_menu = self.group_page.top_menu_open()
        top_menu.log_out_click()
        self.login_page.auto_login(coordinator)
        self.group_page.select_group(group_name)
        left_menu = self.group_page.left_menu_open()
        left_menu.edit_group().click()
        self.assertEqual(self.driver.current_url, edit_group_url)


class TestGroupPageTeacher(unittest.TestCase):
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        cls.driver.get(PathUrl().URL_SITE)
        cls.login_page = LogInPage(cls.driver)
        cls.driver.maximize_window()
        cls.login_page.auto_login(teacher)
        cls.group_page = GroupsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.get('http://localhost:3000/Groups/Dnipro')

    def test28_disabled_create_button_for_teacher(self):
        left_menu = self.group_page.left_menu_open()
        try:
            left_menu.create_group().is_displayed()
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test29_disabled_delete_button_for_teacher(self):
        self.group_page.select_group(group_name)
        left_menu = self.group_page.left_menu_open()
        try:
            left_menu.delete_group().is_displayed()
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)

    def test30_disabled_left_menu_edit_button_for_teacher(self):
        self.group_page.select_group(group_name)
        left_menu = self.group_page.left_menu_open()

        try:
            left_menu.edit_group().is_displayed()
            self.assertTrue(False)
        except Exception:
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
