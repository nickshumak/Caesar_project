
import unittest
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from caesar_items.pages.login_page import LogInPage
from caesar_items.pages.groups_page import GroupsPage
from caesar_items.pages.students_page import StudentsPage


class TestBaseSetUP(unittest.TestCase):

    @classmethod
    def setUpClass(cls, user="", group=""):
        """ Log in as, open top menu,select
        button 'students' and select group."""
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().CHROME_DRIVER)
        cls.driver.get(PathUrl().SITE_URL)
        cls.driver.maximize_window()
        cls.login_page = LogInPage(cls.driver)
        cls.login_page.auto_login(user)
        cls.main_page = GroupsPage(cls.driver)
        cls.main_page.open_top_menu()
        cls.main_page.top_menu.click_students_button()
        cls.main_page.select_group_by_name(group)
        cls.students_page = StudentsPage(cls.driver)
