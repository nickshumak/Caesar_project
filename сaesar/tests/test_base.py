import unittest
from selenium import webdriver
from resource.site_url import PathUrl
from resource.path_driver import GetDriver
from caesar_items.pages.login_page import LogInPage
from caesar_items.pages.groups_page import GroupsPage
from caesar_items.pages.admin_page import AdminPage


class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=GetDriver.CHROME_DRIVER)
        self.driver.get(PathUrl.URL_SITE)
        self.driver.maximize_window()
        self.login_page = LogInPage(self.driver)
        self.group_page = GroupsPage(self.driver)
        self.admin_page = AdminPage(self.driver)

    def tearDown(self):
        self.driver.quit()

