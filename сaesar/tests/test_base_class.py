import unittest
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from caesar_items.pages.login_page import LogInPage
from caesar_items.pages.groups_page import GroupsPage, TopMenu



class TestBaseClass(unittest.TestCase):

    @staticmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        cls.driver.get(PathUrl().URL_SITE)
        cls.driver.maximize_window()
        cls.login_page = LogInPage(cls.driver)
        cls.group_page = GroupsPage(cls.driver)
        cls.top_menu = TopMenu(cls.driver)

