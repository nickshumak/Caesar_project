import unittest
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from caesar_items.pages.login_page import LogInPage
from caesar_items.pages.groups_page import GroupsPage
from caesar_items.pages.students_page import StudentsPage
from resource.data_for_test_suit_students_page import data


class TestBaseSetUP(unittest.TestCase):

    @classmethod
    def setUpClass(cls, user=""):
        """ Log in as specified user, open top menu,select
        button 'students' and select specified group."""
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().CHROME_DRIVER)
        cls.driver.get(PathUrl().SITE_URL)
        cls.driver.maximize_window()
        cls.login_page = LogInPage(cls.driver)
        cls.login_page.auto_login(user)
        cls.main_page = GroupsPage(cls.driver)
        cls.top_menu = cls.main_page.open_top_menu()
        cls.top_menu.click_students_button()
        GroupsPage(cls.driver).select_group_by_name(data['group_name'])
        cls.students_page = StudentsPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        """Close browser."""
        cls.driver.quit()

    def tearDown(self):
        """Go to the test start page."""
        self.driver.get(data['url_for_test_start'])
        self.students_page = StudentsPage(self.driver)
