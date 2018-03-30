import unittest
from selenium import webdriver
from resource.url_site import PathUrl
from resource.path_driver import GetDriver
from caesar_items.pages.login_page import LogInPage


class TestBase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=GetDriver().DRIVER_CHROME)
        self.driver.get(PathUrl().URL_SITE)
        self.driver.maximize_window()
        self.login_page = LogInPage(self.driver)

    def tearDown(self):
        self.driver.quit()

